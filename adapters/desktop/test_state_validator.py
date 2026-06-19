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

from state_machine.state_validator import StateValidator

validator = StateValidator()

result = validator.validate(
    "Bluetooth & devices",
    "Bluetooth & devices"
)

print(
    "Validation:",
    result
)