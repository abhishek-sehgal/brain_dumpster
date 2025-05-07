from datetime import date, timedelta

from animations import done_animation
from storage import save_dump


def get_day(day_str):
    today = date.today()
    if day_str == "today":
        return today.isoformat()
    elif day_str == "yesterday":
        return (today - timedelta(days=1)).isoformat()
    return None


def show_day(goals, label="Goals"):
    print(f"\n📅 {label}:")
    for i, goal in enumerate(goals, 1):
        status = "✅" if goal.get("done") else "❌"
        print(f"  {status} {i}. {goal['text']}")


def collect_goals():
    print("\n🧠 What’s in your brain today?")
    return [
        {"text": input(f"  Goal {i}: ").strip(), "done": False} for i in range(1, 4)
    ]


def mark_goal_done(data, index, day_str):
    day = get_day(day_str)
    if not day or day not in data:
        print(f"⚠️ No brain dump found for {day_str}.")
        return

    goals = data[day]["goals"]
    if 1 <= index <= len(goals):
        goals[index - 1]["done"] = True
        save_dump(data)
        done_animation()
        print(f"✅ Goal {index} from {day_str} marked as done!")
        show_day(goals, label=f"{day_str.capitalize()}'s Goals")
    else:
        print(f"⚠️ Invalid goal number. Only {len(goals)} goals in {day_str}.")


def list_goals(data, day_str):
    day = get_day(day_str)
    if not day or day not in data:
        print(f"⚠️ No brain dump found for {day_str}.")
        return
    show_day(data[day]["goals"], label=f"{day_str.capitalize()}'s Goals")
