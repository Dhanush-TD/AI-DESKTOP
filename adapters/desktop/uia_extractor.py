import uiautomation as auto
from models import UIElement


class UIExtractor:

    def get_settings_elements(self):

        elements = []

        settings_window = auto.WindowControl(
            searchDepth=1,
            Name="Settings"
        )

        if not settings_window.Exists(3):
            print("Settings window not found")
            return elements

        self._walk(settings_window, elements)

        return elements

    def _walk(self, control, elements):

        try:

            element = UIElement(
                name=control.Name,
                control_type=control.ControlTypeName,
                automation_id=control.AutomationId,
                class_name=control.ClassName
            )

            elements.append(element)

        except Exception:
            pass

        try:
            for child in control.GetChildren():
                self._walk(child, elements)
        except Exception:
            pass