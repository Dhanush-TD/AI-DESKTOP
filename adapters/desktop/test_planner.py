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

from state_machine.navigation_planner import NavigationPlanner

planner = NavigationPlanner()

plan = planner.plan(
    "Home",
    "Bluetooth"
)

print(plan)