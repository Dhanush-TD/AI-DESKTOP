import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from validation.window_validator import (
    WindowValidator
)

validator = WindowValidator()

result = validator.exists(
    "Add a device"
)

print(
    "\nWindow Exists:\n"
)

print(result)