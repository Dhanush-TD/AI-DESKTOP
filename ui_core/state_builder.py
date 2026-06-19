from ui_core.ui_state_manager import UIState


class StateBuilder:

    VALID_NAV_ITEMS = {
        "Home",
        "System",
        "Bluetooth & devices",
        "Network & internet",
        "Personalization",
        "Apps",
        "Accounts",
        "Time & language",
        "Gaming",
        "Accessibility",
        "Privacy & security",
        "Windows Update"
    }

    def build(self, elements):

        page_title = "Unknown"

        actions = []

        # ----------------------------
        # Detect Current Page
        # ----------------------------

        breadcrumb_items = []

        for element in elements:

            if (
                element.control_type == "ButtonControl"
                and
                element.class_name ==
                "Microsoft.UI.Xaml.Controls.BreadcrumbBarItem"
                and
                element.name
            ):

                breadcrumb_items.append(
                    element.name
                )

        if breadcrumb_items:

            page_title = breadcrumb_items[-1]

        # ----------------------------
        # Detect Available Actions
        # ----------------------------

        for element in elements:

            if (
                element.control_type ==
                "ListItemControl"
            ):

                if (
                    element.name in
                    self.VALID_NAV_ITEMS
                ):

                    actions.append(
                        element.name
                    )

        return UIState(
            screen_name="Settings",
            page_title=page_title,
            actions=actions
        )