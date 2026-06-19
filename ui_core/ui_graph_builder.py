import networkx as nx


class UIGraphBuilder:

    def build(self, elements):

        graph = nx.DiGraph()

        root = "SETTINGS_WINDOW"

        graph.add_node(
            root,
            name="Settings",
            type="Root"
        )

        for element in elements:

            node_id = f"{element.control_type}:{element.name}"

            graph.add_node(
                node_id,
                name=element.name,
                type=element.control_type
            )

            graph.add_edge(root, node_id)

        return graph