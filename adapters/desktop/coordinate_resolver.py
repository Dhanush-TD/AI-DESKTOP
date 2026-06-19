import uiautomation as auto


class CoordinateResolver:

    def find_element_center(
        self,
        text
    ):

        settings_window = auto.WindowControl(
            searchDepth=1,
            Name="Settings"
        )

        if not settings_window.Exists(3):
            return None

        for control, depth in auto.WalkControl(
            settings_window,
            maxDepth=20
        ):

            try:

                if (
                    control.Name.lower() ==
                    text.lower()
                ):

                    rect = (
                        control.BoundingRectangle
                    )

                    center_x = (
                        rect.left +
                        rect.right
                    ) // 2

                    center_y = (
                        rect.top +
                        rect.bottom
                    ) // 2

                    return (
                        center_x,
                        center_y
                    )

            except Exception:
                pass

        return None