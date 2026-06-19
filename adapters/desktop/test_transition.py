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

from state_machine.transition_engine import TransitionEngine

engine = TransitionEngine()

next_state = engine.get_next_state(
    "Home",
    "Bluetooth & devices"
)

print(
    "Next State:",
    next_state
)