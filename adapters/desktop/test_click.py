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

from adapters.desktop.click_executor import (
    ClickExecutor
)

executor = ClickExecutor()

print(
    "\nMouse will move in 3 seconds..."
)

input(
    "Press ENTER to continue..."
)

executor.click(
    500,
    500
)

print(
    "\nClick completed"
)