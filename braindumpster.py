import json
import sys
import time
from datetime import date
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


def get_today():
    return date.today().isoformat()


def get_yesterday(data):
    dates = sorted(data.keys())
    if dates:
        return dates[-1]
    return None


def show_yesterday(data):
    yesterday = get_yesterday(data)
    if not yesterday or yesterday == get_today():
        return
    print(f"\n📅 Yesterday's Dump ({yesterday}):")
    for i, goal in enumerate(data[yesterday]["goals"], 1):
        status = "✅" if goal.get("done") else "❌"
        print(f"  {status} {i}. {goal['text']}")


def collect_goals():
    print("\n🧠 What’s in your brain today?")
    goals = []
    for i in range(1, 4):
        text = input(f"  Goal {i}: ").strip()
        goals.append({"text": text, "done": False})
    return goals


def dump_animation():
    sparkle = ["💭", "🗑️", "🌀", "✨", "💡"]
    for i in range(5):
        sys.stdout.write("\rDumping brain " + sparkle[i % len(sparkle)] * (i + 1))
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write("\r" + " " * 40 + "\r")
    print("🧻 Brain successfully dumped ✨")


def main():
    data = load_dump()
    today = get_today()

    if today in data:
        print("\n📌 You already dumped your brain today!")
        show_yesterday(data)
        return

    show_yesterday(data)
    goals = collect_goals()
    data[today] = {"goals": goals}
    save_dump(data)
    dump_animation()


if __name__ == "__main__":
    print("\n🧠 Welcome to BrainDumpster!")
    main()
