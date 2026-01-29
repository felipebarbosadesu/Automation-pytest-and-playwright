import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

from tests.config.settings import get_settings
from tests.utils.naming import safe_test_name

ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
VIDEOS_DIR = ARTIFACTS_DIR / "videos"
TRACES_DIR = ARTIFACTS_DIR / "traces"

def _ensure_dirs():
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    TRACES_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "reports").mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session")
def settings():
    return get_settings()

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright, settings):
    browser = playwright.chromium.launch(
        headless=settings["headless"],
        slow_mo=settings["slow_mo"],
    )
    yield browser
    browser.close()

@pytest.fixture()
def context(browser, request):
    _ensure_dirs()

    ctx = browser.new_context(
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 1280, "height": 720},
    )

    # Trace is a full replay (steps, network, snapshots)
    ctx.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield ctx

    name = safe_test_name(request.node.name)
    ctx.tracing.stop(path=str(TRACES_DIR / f"{name}.zip"))
    ctx.close()

@pytest.fixture()
def page(context, settings):
    p = context.new_page()
    p.set_default_timeout(10_000)
    p.goto(settings["base_url"])
    yield p
    p.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Screenshot only on failure
    if rep.when == "call" and rep.failed:
        _ensure_dirs()
        page = item.funcargs.get("page")
        if page:
            name = safe_test_name(item.name)
            page.screenshot(path=str(SCREENSHOTS_DIR / f"{name}.png"), full_page=True)
