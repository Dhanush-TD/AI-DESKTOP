class Validator:

    def validate(
        self,
        match
    ):

        if match is None:
            return False

        node_id, data, score = match

        if score < 100:
            return False

        if not data["name"]:
            return False

        return True