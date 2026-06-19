import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from adapters.desktop.uia_extractor import UIExtractor
from ui_core.state_builder import StateBuilder


extractor = UIExtractor()

elements = extractor.get_settings_elements()

builder = StateBuilder()

state = builder.build(
    elements
)

print(state)