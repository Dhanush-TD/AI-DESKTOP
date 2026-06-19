from dataclasses import dataclass


@dataclass
class UIElement:
    name: str
    control_type: str
    automation_id: str
    class_name: str