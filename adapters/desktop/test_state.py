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

from ui_core.ui_state_manager import UIState

state = UIState(
    screen_name="Settings",
    page_title="Home",
    actions=[
        "System",
        "Bluetooth & devices",
        "Network & internet",
        "Apps"
    ]
)

print(state)