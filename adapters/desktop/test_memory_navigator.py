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

from memory.memory_navigator import (
    MemoryNavigator
)

navigator = (
    MemoryNavigator()
)

steps = navigator.get_steps(
    "connect earbuds"
)

print("\nMemory Steps:\n")

for step in steps:

    print(step)