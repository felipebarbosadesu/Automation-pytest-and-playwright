import os
from dotenv import load_dotenv
from .environments import ENVIRONMENTS

load_dotenv()

def get_settings():
    env = os.getenv("ENV", "dev").strip()
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    slow_mo = int(os.getenv("SLOW_MO", "0") or "0")

    if env not in ENVIRONMENTS:
        env = "dev"

    base_url = ENVIRONMENTS[env]["base_url"]

    return {
        "env": env,
        "headless": headless,
        "slow_mo": slow_mo,
        "base_url": base_url,
    }
