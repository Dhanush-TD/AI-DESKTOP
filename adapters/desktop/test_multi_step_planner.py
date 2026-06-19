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

from state_machine.multi_step_planner import (
    MultiStepPlanner
)

planner = MultiStepPlanner()

steps = planner.plan(

    "Home",

    [
        "Bluetooth & devices",
        "Add device"
    ]
)

for step in steps:

    print(step)