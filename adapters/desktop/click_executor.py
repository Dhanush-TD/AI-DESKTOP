import pyautogui


class ClickExecutor:

    def click(
        self,
        x,
        y
    ):

        pyautogui.moveTo(
            x,
            y,
            duration=0.3
        )

        pyautogui.click()