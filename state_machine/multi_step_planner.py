from state_machine.navigation_graph import (
    NavigationGraph
)


class MultiStepPlanner:

    def __init__(self):

        self.graph = NavigationGraph()

    def plan(
        self,
        current_state,
        target_sequence
    ):

        steps = []

        state = current_state

        for target in target_sequence:

            node = self.graph.get_next(
                state,
                target
            )

            if not node:
                continue

            steps.append({

                "from":
                    state,

                "action":
                    node["action"],

                "to":
                    node["next_state"]
            })

            state = (
                node["next_state"]
            )

        return steps