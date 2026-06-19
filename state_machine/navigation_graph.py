class NavigationGraph:

    GRAPH = {

        "Home": {

            "Bluetooth & devices": {

                "action":
                    "Bluetooth & devices",

                "next_state":
                    "Bluetooth & devices"
            },

            "Apps": {

                "action":
                    "Apps",

                "next_state":
                    "Apps"
            },

            "Network & internet": {

                "action":
                    "Network & internet",

                "next_state":
                    "Network & internet"
            },

            "Windows Update": {

                "action":
                    "Windows Update",

                "next_state":
                    "Windows Update"
            }
        },

        "Bluetooth & devices": {

            "Add device": {

                "action":
                    "Add device",

                "next_state":
                    "Add a device"
            },

            "View more devices": {

                "action":
                    "View more devices",

                "next_state":
                    "View more devices"
            }
        },

        "Apps": {

            "Installed apps": {

                "action":
                    "Installed apps",

                "next_state":
                    "Installed apps"
            }
        }
    }

    def get_next(
        self,
        current_state,
        target
    ):

        if current_state not in self.GRAPH:
            return None

        return self.GRAPH[
            current_state
        ].get(target)