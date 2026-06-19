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

from memory.memory_orchestrator import (
    MemoryOrchestrator
)

orchestrator = (
    MemoryOrchestrator()
)

steps = orchestrator.get_workflow(
    "pair earbuds"
)

print(
    "\nWorkflow From Memory:\n"
)

for step in steps:

    print(step)