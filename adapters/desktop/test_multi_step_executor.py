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

from state_machine.multi_step_executor import (
    MultiStepExecutor
)

from adapters.desktop.coordinate_resolver import (
    CoordinateResolver
)

from adapters.desktop.click_executor import (
    ClickExecutor
)

from state_machine.live_state_detector import (
    LiveStateDetector
)

from validation.universal_validator import (
    UniversalValidator
)

planner = MultiStepPlanner()

steps = planner.plan(

    "Home",

    [
        "Bluetooth & devices",
        "Add device"
    ]
)

executor = MultiStepExecutor(

    CoordinateResolver(),

    ClickExecutor(),

    LiveStateDetector(),

    UniversalValidator()
)

input(
    "\nOpen Settings Home Page and press ENTER..."
)

results = (
    executor.execute_steps(
        steps
    )
)

print("\nResults\n")

for result in results:

    print(result)