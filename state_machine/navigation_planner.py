class NavigationPlanner:

    def plan(
        self,
        current_state,
        mapped_goal
    ):

        if mapped_goal is None:
            return None

        return {

            "current_state":
                current_state,

            "action":
                mapped_goal,

            "target_state":
                mapped_goal
        }