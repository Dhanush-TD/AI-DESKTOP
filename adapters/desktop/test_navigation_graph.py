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

from state_machine.navigation_graph import (
    NavigationGraph
)

graph = NavigationGraph()

result = graph.get_next(
    "Bluetooth & devices",
    "Add device"
)

print(result)