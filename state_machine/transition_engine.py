class TransitionEngine:

    def __init__(self):

        self.transitions = {

            ("Home", "System"):
                "System",

            ("Home", "Bluetooth & devices"):
                "Bluetooth & devices",

            ("Home", "Network & internet"):
                "Network & internet",

            ("Home", "Apps"):
                "Apps",

            ("Home", "Personalization"):
                "Personalization",

            ("Home", "Accounts"):
                "Accounts",

            ("Home", "Accessibility"):
                "Accessibility",

            ("Home", "Windows Update"):
                "Windows Update"
        }

    def get_next_state(
        self,
        current_state,
        action
    ):

        return self.transitions.get(
            (current_state, action),
            None
        )