class RecoveryEngine:

    def recover(
        self,
        expected_state,
        actual_state
    ):

        if (
            expected_state ==
            actual_state
        ):

            return {
                "recovered": False,
                "reason": "No recovery needed"
            }

        return {

            "recovered": True,

            "action":
                "retry_navigation",

            "expected":
                expected_state,

            "actual":
                actual_state
        }
    