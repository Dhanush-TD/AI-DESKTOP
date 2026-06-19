from memory.memory_manager import (
    MemoryManager
)

from memory.workflow_converter import (
    WorkflowConverter
)

from memory.learning_engine import (
    LearningEngine
)


class MemoryOrchestrator:

    def __init__(self):

        self.memory = (
            MemoryManager()
        )

        self.converter = (
            WorkflowConverter()
        )

        self.learning = (
            LearningEngine()
        )

    def get_workflow(
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
        steps,
        success
    ):

        return (
            self.learning.learn(
                goal,
                steps,
                success
            )
        )