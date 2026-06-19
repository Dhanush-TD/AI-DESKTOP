class Ranker:

    def best_match(
        self,
        results,
        query
    ):

        query = query.lower()

        best = None
        best_score = -1

        for node_id, data in results:

            score = 0

            control_type = data["type"]

            if control_type == "ButtonControl":
                score += 50

            elif control_type == "ListItemControl":
                score += 40

            elif control_type == "HyperlinkControl":
                score += 30

            elif control_type == "TextControl":
                score += 10

            name = data["name"].lower()

            if name == query:
                score += 100

            elif query in name:
                score += 50

            score += (
                len(query) /
                max(len(name), 1)
            ) * 10

            if score > best_score:
                best_score = score
                best = (
                    node_id,
                    data,
                    score
                )

        return best