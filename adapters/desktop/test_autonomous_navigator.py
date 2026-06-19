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

from state_machine.autonomous_navigator import (
    AutonomousNavigator
)

from matching.semantic_goal_matcher import (
    SemanticGoalMatcher
)

from state_machine.navigation_planner import (
    NavigationPlanner
)

from state_machine.live_state_detector import (
    LiveStateDetector
)

from state_machine.state_validator import (
    StateValidator
)

from adapters.desktop.coordinate_resolver import (
    CoordinateResolver
)

from adapters.desktop.click_executor import (
    ClickExecutor
)

from fallback_engine.recovery_engine import (
    RecoveryEngine
)

navigator = AutonomousNavigator(
    SemanticGoalMatcher(),
    NavigationPlanner(),
    CoordinateResolver(),
    ClickExecutor(),
    LiveStateDetector(),
    StateValidator(),
    RecoveryEngine()
)

input(
    "\nOpen Settings Home Page and press ENTER..."
)

result = navigator.execute(
    "connect earbuds",
    "Home"
)

print("\nResult\n")

print(result)