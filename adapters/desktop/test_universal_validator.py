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

from validation.universal_validator import (
    UniversalValidator
)

validator = UniversalValidator()

print(
    validator.validate(
        "Add a device",
        "Bluetooth & devices"
    )
)