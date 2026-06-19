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

from memory.workflow_memory import (
    WorkflowMemory
)

memory = WorkflowMemory()

memory.save_workflow(

    "connect earbuds",

    [
        {
            "action":
                "Bluetooth & devices"
        },

        {
            "action":
                "Add device"
        }
    ]
)

workflow = memory.get_workflow(
    "connect earbuds"
)

print(
    "\nWorkflow:\n"
)

print(workflow)