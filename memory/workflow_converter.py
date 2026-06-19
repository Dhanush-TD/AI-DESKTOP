class WorkflowConverter:

    def memory_to_steps(
        self,
        workflow
    ):

        steps = []

        current_state = "Unknown"

        for item in workflow:

            next_state = item.get(
                "next_state",
                item["action"]
            )

            steps.append({

                "from":
                    current_state,

                "action":
                    item["action"],

                "to":
                    next_state
            })

            current_state = (
                next_state
            )

        return steps