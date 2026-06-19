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

from matching.semantic_goal_matcher import (
    SemanticGoalMatcher
)

matcher = SemanticGoalMatcher()

tests = [

    "connect earbuds",
    "bluetooth settings",
    "wifi",
    "installed apps",
    "check updates"
]

for test in tests:

    page, score = matcher.match(
        test
    )

    print(
        f"\nGoal: {test}"
    )

    print(
        f"Match: {page}"
    )

    print(
        f"Score: {round(score,2)}"
    )