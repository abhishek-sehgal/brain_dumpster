import json
from pathlib import Path

DUMP_FILE = Path("brain_dump.json")


def load_dump():
    if DUMP_FILE.exists():
        with open(DUMP_FILE, "r") as f:
            return json.load(f)
    return {}


def save_dump(data):
    with open(DUMP_FILE, "w") as f:
        json.dump(data, f, indent=2)
