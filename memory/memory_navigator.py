from memory.memory_manager import (
    MemoryManager
)

from memory.workflow_converter import (
    WorkflowConverter
)


class MemoryNavigator:

    def __init__(self):

        self.memory = (
            MemoryManager()
        )

        self.converter = (
            WorkflowConverter()
        )

    def get_steps(
        self,
        goal
    ):

        workflow = (
            self.memory.lookup(
                goal
            )
        )

        if not workflow:

            return None

        return (
            self.converter.memory_to_steps(
                workflow
            )
        )

    def learn(
        self,
        goal,
        workflow
    ):

        self.memory.learn(
            goal,
            workflow
        )