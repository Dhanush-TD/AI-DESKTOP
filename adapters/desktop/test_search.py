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
from matching.ranker import Ranker

from adapters.desktop.uia_extractor import UIExtractor
from ui_core.ui_graph_builder import UIGraphBuilder
from matching.graph_search import GraphSearch


extractor = UIExtractor()

elements = extractor.get_settings_elements()

builder = UIGraphBuilder()

graph = builder.build(elements)

search = GraphSearch()

results = search.find_by_name(
    graph,
    "Bluetooth"
)

ranker = Ranker()

best = ranker.best_match(
    results,
    "Bluetooth"
)

print("\nBest Match:\n")

print(best)

