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
from state_machine.navigation_planner import NavigationPlanner
from state_machine.transition_engine import TransitionEngine


goal = "pair device"

mapper = GoalMapper()

mapped_goal = mapper.map_goal(
    goal
)

planner = NavigationPlanner()

plan = planner.plan(
    "Home",
    mapped_goal
)

engine = TransitionEngine()

next_state = engine.get_next_state(
    "Home",
    plan["action"]
)

print("\nGoal:")
print(goal)

print("\nMapped Goal:")
print(mapped_goal)

print("\nPlan:")
print(plan)

print("\nPredicted State:")
print(next_state)