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

from memory.learning_engine import (
    LearningEngine
)

from memory.memory_manager import (
    MemoryManager
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

engine = LearningEngine()

engine.learn(
    "pair earbuds",
    steps,
    True
)

memory = MemoryManager()

workflow = memory.lookup(
    "pair earbuds"
)

print("\nLearned Workflow:\n")

for item in workflow:

    print(item)