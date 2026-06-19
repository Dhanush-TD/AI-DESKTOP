from memory.memory_manager import (
    MemoryManager
)

from memory.workflow_serializer import (
    WorkflowSerializer
)


class LearningEngine:

    def __init__(self):

        self.memory = (
            MemoryManager()
        )

        self.serializer = (
            WorkflowSerializer()
        )

    def learn(
        self,
        goal,
        steps,
        success
    ):

        if not success:
            return False

        workflow = (
            self.serializer.serialize(
                steps
            )
        )

        self.memory.learn(
            goal,
            workflow
        )

        return True