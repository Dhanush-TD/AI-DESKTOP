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

from memory.memory_manager import (
    MemoryManager
)

manager = MemoryManager()

workflow = manager.lookup(
    "connect earbuds"
)

print(
    "\nMemory Lookup:\n"
)

print(workflow)