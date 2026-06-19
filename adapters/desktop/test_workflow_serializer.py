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

from memory.workflow_serializer import (
    WorkflowSerializer
)

steps = [

    {
        "from": "Home",
        "action": "Bluetooth & devices",
        "to": "Bluetooth & devices"
    },

    {
        "from": "Bluetooth & devices",
        "action": "Add device",
        "to": "Add a device"
    }
]

serializer = (
    WorkflowSerializer()
)

workflow = (
    serializer.serialize(
        steps
    )
)

print("\nWorkflow:\n")

for item in workflow:

    print(item)