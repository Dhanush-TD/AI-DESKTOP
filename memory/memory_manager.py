from memory.workflow_memory import (
    WorkflowMemory
)


class MemoryManager:

    def __init__(self):

        self.memory = (
            WorkflowMemory()
        )

    def lookup(
        self,
        goal
    ):

        return self.memory.get_workflow(
            goal
        )

    def learn(
        self,
        goal,
        workflow
    ):

        self.memory.save_workflow(
            goal,
            workflow
        )