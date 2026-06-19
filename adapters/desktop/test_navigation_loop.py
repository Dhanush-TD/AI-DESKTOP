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

from state_machine.navigation_loop import (
    NavigationLoop
)

from state_machine.navigation_planner import (
    NavigationPlanner
)

from state_machine.state_validator import (
    StateValidator
)

from state_machine.live_state_detector import (
    LiveStateDetector
)

loop = NavigationLoop()

planner = NavigationPlanner()

validator = StateValidator()

detector = LiveStateDetector()

result = loop.run(
    "Bluetooth & devices",
    "Home",
    planner,
    validator,
    detector
)

print("\nResult\n")

print(result)