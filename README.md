# Swag Labs (SauceDemo) E2E Web Tests — Pytest + Playwright

Automated end-to-end tests for **https://www.saucedemo.com/** using **Pytest + Playwright** with **Page Object Model** and **evidence collection** (screenshots/videos/traces).

## ✅ What’s covered
- Login (valid users + locked out)
- Add item to cart (smoke)
- Checkout happy path (regression / e2e)
- Evidences on failures (screenshot) + replay (trace) + video

## 🧱 Tech stack
- Python
- Pytest
- Playwright
- Page Object Model
- GitHub Actions CI

## 🚀 Run locally

### 1) Create venv + install deps
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
playwright install
```

### 2) Configure env
Copy `.env.example` to `.env` (local only):
```bash
cp .env.example .env
```

### 3) Run tests
```bash
pytest
```

### Run only smoke
```bash
pytest -m smoke
```

### Run regression
```bash
pytest -m regression
```

### Generate HTML report
```bash
pytest --html=artifacts/reports/report.html --self-contained-html
```

## 📸 Evidences (Artifacts)
On failure, a screenshot is saved to:
- `artifacts/screenshots/`

For every test run, Playwright also saves:
- video: `artifacts/videos/`
- trace: `artifacts/traces/` (open with `playwright show-trace <file.zip>`)

## 🔐 Test credentials (SauceDemo)
Accepted usernames:
- `standard_user`
- `locked_out_user`
- `problem_user`
- `performance_glitch_user`
- `error_user`
- `visual_user`

Password for all users:
- `secret_sauce`

## 🤖 CI (GitHub Actions)
Workflow file:
- `.github/workflows/tests.yml`

It runs tests on push/PR and uploads `artifacts/` as build artifacts.
