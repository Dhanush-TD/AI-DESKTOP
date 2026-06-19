from memory.memory_orchestrator import (
    MemoryOrchestrator
)


class MemoryAwareNavigator:

    def __init__(
        self,
        planner,
        executor
    ):

        self.memory = (
            MemoryOrchestrator()
        )

        self.planner = planner

        self.executor = executor

    def execute_goal(
        self,
        goal,
        current_state,
        target_sequence
    ):

        memory_steps = (
            self.memory.get_workflow(
                goal
            )
        )

        if memory_steps:

            print(
                "\nMEMORY HIT"
            )

            return self.executor.execute_steps(
                memory_steps
            )

        print(
            "\nMEMORY MISS"
        )

        steps = self.planner.plan(
            current_state,
            target_sequence
        )

        results = (
            self.executor.execute_steps(
                steps
            )
        )

        success = all(

            result.get(
                "success",
                False
            )

            for result in results
        )

        self.memory.learn(
            goal,
            steps,
            success
        )

        return results