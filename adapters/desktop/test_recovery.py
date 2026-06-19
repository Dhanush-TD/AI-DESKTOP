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

from fallback_engine.recovery_engine import (
    RecoveryEngine
)

engine = RecoveryEngine()

result = engine.recover(
    "Bluetooth & devices",
    "Home"
)

print(result)