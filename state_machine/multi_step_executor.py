import time


class MultiStepExecutor:

    def __init__(
        self,
        resolver,
        executor,
        detector,
        validator
    ):

        self.resolver = resolver
        self.executor = executor
        self.detector = detector
        self.validator = validator

    def execute_steps(
        self,
        steps
    ):

        results = []

        for step in steps:

            print(
                f"\nExecuting: {step['action']}"
            )

            coords = (
                self.resolver.find_element_center(
                    step["action"]
                )
            )

            if not coords:

                results.append({

                    "step": step,

                    "success": False,

                    "reason":
                        "Element not found"
                })

                continue

            self.executor.click(
                coords[0],
                coords[1]
            )

            time.sleep(1)

            state = (
                self.detector.detect()
            )

            success = (
                self.validator.validate(
                    step["to"],
                    state.page_title
                )
            )

            results.append({

                "step": step,

                "actual":
                    state.page_title,

                "success":
                    success
            })

        return results