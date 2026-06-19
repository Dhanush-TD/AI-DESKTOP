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

from state_machine.goal_mapper import GoalMapper

mapper = GoalMapper()

print(
    mapper.map_goal(
        "pair device"
    )
)