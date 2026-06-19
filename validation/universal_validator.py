from validation.window_validator import (
    WindowValidator
)


class UniversalValidator:

    def __init__(self):

        self.window_validator = (
            WindowValidator()
        )

    def validate(
        self,
        expected,
        actual_page
    ):

        if (
            expected.lower()
            ==
            actual_page.lower()
        ):

            return True

        if (
            self.window_validator.exists(
                expected
            )
        ):

            return True

        return False