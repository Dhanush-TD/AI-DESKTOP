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

from adapters.desktop.uia_extractor import UIExtractor
from ui_core.ui_graph_builder import UIGraphBuilder

extractor = UIExtractor()

elements = extractor.get_settings_elements()

builder = UIGraphBuilder()

graph = builder.build(elements)

print("\nGraph Statistics\n")

print("Nodes:", graph.number_of_nodes())
print("Edges:", graph.number_of_edges())

print("\nFirst 20 Nodes:\n")

for node in list(graph.nodes(data=True))[:20]:
    print(node)