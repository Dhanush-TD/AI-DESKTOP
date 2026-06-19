import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from state_machine.live_state_detector import (
    LiveStateDetector
)

detector = LiveStateDetector()

state = detector.detect()

print("\nCurrent State\n")

print("Screen:", state.screen_name)
print("Page:", state.page_title)

print("Actions:")

for action in state.actions:
    print("-", action)