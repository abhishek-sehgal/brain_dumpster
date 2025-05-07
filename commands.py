from datetime import date

from animations import dump_animation
from goals import collect_goals, get_day, list_goals, mark_goal_done, show_day
from storage import load_dump, save_dump
from utils import print_help


def handle_args(args):
    data = load_dump()

    if "--help" in args:
        print_help()
        return

    if "--list" in args:
        day_arg = (
            args[args.index("--list") + 1]
            if len(args) > args.index("--list") + 1
            else "today"
        )
        list_goals(data, day_arg)
        return

    if args and args[0] == "--done":
        try:
            index = int(args[1])
            day_arg = "today"
            if "--day" in args:
                day_arg = args[args.index("--day") + 1]
            mark_goal_done(data, index, day_arg)
        except (IndexError, ValueError):
            print("Usage: python main.py --done <goal_number> [--day today|yesterday]")
        return

    today = get_day("today")
    if today in data:
        print("\n📌 You already dumped your brain today!")
        show_day(data[today]["goals"])
        return

    goals = collect_goals()
    data[today] = {"goals": goals}
    save_dump(data)
    dump_animation()
