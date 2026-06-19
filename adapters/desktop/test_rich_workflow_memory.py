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

    "pair earbuds",

    [

        {
            "action":
                "Bluetooth & devices",

            "next_state":
                "Bluetooth & devices"
        },

        {
            "action":
                "Add device",

            "next_state":
                "Add a device"
        }
    ]
)

workflow = (
    memory.get_workflow(
        "pair earbuds"
    )
)

print("\nWorkflow:\n")

for step in workflow:

    print(step)