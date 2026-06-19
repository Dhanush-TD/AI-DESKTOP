from difflib import SequenceMatcher


class SemanticGoalMatcher:

    GOALS = {

        "Bluetooth & devices": [

            "bluetooth",
            "pair device",
            "connect earbuds",
            "connect headphones",
            "wireless devices",
            "bluetooth settings",
            "connect speaker"
        ],

        "Network & internet": [

            "wifi",
            "internet",
            "network",
            "connect wifi",
            "wireless network"
        ],

        "Apps": [

            "apps",
            "installed apps",
            "uninstall app",
            "manage apps"
        ],

        "Windows Update": [

            "update",
            "windows update",
            "check updates"
        ]
    }

    def match(self, user_goal):

        user_goal = user_goal.lower()

        best_page = None
        best_score = 0

        for page, phrases in self.GOALS.items():

            for phrase in phrases:

                score = SequenceMatcher(
                    None,
                    user_goal,
                    phrase.lower()
                ).ratio()

                if score > best_score:

                    best_score = score
                    best_page = page

        return best_page, best_score