class WorkflowSerializer:

    def serialize(
        self,
        steps
    ):

        workflow = []

        for step in steps:

            workflow.append({

                "action":
                    step["action"],

                "next_state":
                    step["to"]
            })

        return workflow