class UIState:

    def __init__(
        self,
        screen_name,
        page_title,
        actions
    ):
        self.screen_name = screen_name
        self.page_title = page_title
        self.actions = actions

    def __repr__(self):

        return (
            f"\nScreen: {self.screen_name}\n"
            f"Page: {self.page_title}\n"
            f"Actions: {self.actions}\n"
        )