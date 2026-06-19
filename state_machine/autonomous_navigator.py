import time


class AutonomousNavigator:

    def __init__(
        self,
        matcher,
        planner,
        resolver,
        executor,
        detector,
        validator,
        recovery_engine
    ):

        self.matcher = matcher
        self.planner = planner
        self.resolver = resolver
        self.executor = executor
        self.detector = detector
        self.validator = validator
        self.recovery_engine = recovery_engine

    def execute(
        self,
        user_goal,
        current_state
    ):

        mapped_goal, score = (
            self.matcher.match(
                user_goal
            )
        )

        if not mapped_goal:

            return {
                "success": False,
                "reason": "No match found"
            }

        plan = self.planner.plan(
            current_state,
            mapped_goal
        )

        coords = (
            self.resolver.find_element_center(
                plan["action"]
            )
        )

        if not coords:

            return {
                "success": False,
                "reason": "Element not found"
            }

        print(
            f"\nMatched: {mapped_goal}"
        )

        print(
            f"Confidence: {round(score,2)}"
        )

        # First Attempt

        self.executor.click(
            coords[0],
            coords[1]
        )

        time.sleep(1)

        live_state = (
            self.detector.detect()
        )

        success = (
            self.validator.validate(
                plan["target_state"],
                live_state.page_title
            )
        )

        # Recovery Attempt

        if not success:

            recovery = (
                self.recovery_engine.recover(
                    plan["target_state"],
                    live_state.page_title
                )
            )

            print(
                "\nRecovery Triggered"
            )

            print(recovery)

            self.executor.click(
                coords[0],
                coords[1]
            )

            time.sleep(1)

            live_state = (
                self.detector.detect()
            )

            success = (
                self.validator.validate(
                    plan["target_state"],
                    live_state.page_title
                )
            )

        return {

            "goal":
                user_goal,

            "mapped_goal":
                mapped_goal,

            "confidence":
                round(score,2),

            "expected_state":
                plan["target_state"],

            "actual_state":
                live_state.page_title,

            "success":
                success
        }