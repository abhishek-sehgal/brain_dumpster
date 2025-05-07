import sys
import time


def dump_animation():
    sparkle = ["💭", "🗑️", "🌀", "✨", "💡"]
    for i in range(5):
        sys.stdout.write("\rDumping brain " + sparkle[i % len(sparkle)] * (i + 1))
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write("\r" + " " * 40 + "\r")
    print("🧻 Brain successfully dumped ✨")


def done_animation():
    ticks = ["⏳", "🕐", "🕓", "✅"]
    for tick in ticks:
        sys.stdout.write(f"\rMarking as done... {tick}")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write("\r" + " " * 30 + "\r")
    print("🏁 Donezo!")
