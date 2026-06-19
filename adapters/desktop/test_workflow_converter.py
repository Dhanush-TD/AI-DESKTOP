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

from memory.workflow_converter import (
    WorkflowConverter
)

memory = MemoryManager()

workflow = memory.lookup(
    "connect earbuds"
)

converter = (
    WorkflowConverter()
)

steps = (
    converter.memory_to_steps(
        workflow
    )
)

print(
    "\nSteps:\n"
)

for step in steps:

    print(step)