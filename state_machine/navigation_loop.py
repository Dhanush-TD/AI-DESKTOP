class NavigationLoop:

    def run(
        self,
        goal,
        current_state,
        planner,
        validator,
        detector
    ):

        plan = planner.plan(
            current_state,
            goal
        )

        if not plan:
            return {
                "status": "failed"
            }

        print("\nPlan Created")
        print(plan)

        input(
            "\nNavigate manually and press ENTER..."
        )

        live_state = detector.detect()

        success = validator.validate(
            plan["target_state"],
            live_state.page_title
        )

        return {

            "goal": goal,

            "expected_state":
                plan["target_state"],

            "actual_state":
                live_state.page_title,

            "success":
                success
        }