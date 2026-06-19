class StateValidator:

    def validate(
        self,
        expected_state,
        current_state
    ):

        return (
            expected_state ==
            current_state
        )