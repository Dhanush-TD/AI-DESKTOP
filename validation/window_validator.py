import uiautomation as auto


class WindowValidator:

    def exists(
        self,
        window_name
    ):

        root = auto.GetRootControl()

        for control, depth in auto.WalkControl(
            root,
            maxDepth=5
        ):

            try:

                if (
                    control.ControlTypeName
                    == "WindowControl"
                    and
                    control.Name.lower()
                    == window_name.lower()
                ):

                    return True

            except Exception:
                pass

        return False