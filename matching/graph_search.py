class GraphSearch:

    def find_by_name(self, graph, search_text):

        results = []

        search_text = search_text.lower()

        for node_id, data in graph.nodes(data=True):

            name = str(
                data.get("name", "")
            ).lower()

            if search_text in name:

                results.append(
                    (node_id, data)
                )

        return results