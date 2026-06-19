class GoalMapper:

    GOAL_MAP = {

        "bluetooth":
            "Bluetooth & devices",

        "bluetooth settings":
            "Bluetooth & devices",

        "pair device":
            "Bluetooth & devices",

        "network":
            "Network & internet",

        "wifi":
            "Network & internet",

        "internet":
            "Network & internet",

        "apps":
            "Apps",

        "installed apps":
            "Apps",

        "update":
            "Windows Update",

        "windows update":
            "Windows Update"
    }

    def map_goal(
        self,
        goal
    ):

        return self.GOAL_MAP.get(
            goal.lower(),
            None
        )