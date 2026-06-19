import json
import os


class WorkflowMemory:

    FILE_PATH = "memory/workflows.json"

    def __init__(self):

        os.makedirs(
            "memory",
            exist_ok=True
        )

        if not os.path.exists(
            self.FILE_PATH
        ):

            with open(
                self.FILE_PATH,
                "w"
            ) as f:

                json.dump(
                    {},
                    f,
                    indent=4
                )

    def save_workflow(
        self,
        goal,
        steps
    ):

        with open(
            self.FILE_PATH,
            "r"
        ) as f:

            data = json.load(f)

        data[goal] = steps

        with open(
            self.FILE_PATH,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def get_workflow(
        self,
        goal
    ):

        with open(
            self.FILE_PATH,
            "r"
        ) as f:

            data = json.load(f)

        return data.get(goal)