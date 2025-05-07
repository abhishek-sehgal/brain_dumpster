def print_help():
    print("""
🧠 BrainDumpster – Command Line Mind Dump 🗑️

Usage:
  python main.py                            Start a new brain dump for today
  python main.py --done N                   Mark goal N from today as done
  python main.py --done N --day yesterday   Mark goal N from yesterday as done
  python main.py --list today               List today’s goals
  python main.py --list yesterday           List yesterday’s goals
  python main.py --help                     Show this help message
""")
