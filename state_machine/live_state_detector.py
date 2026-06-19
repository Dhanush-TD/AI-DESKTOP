from ui_core.state_builder import StateBuilder
from adapters.desktop.uia_extractor import UIExtractor


class LiveStateDetector:

    def detect(self):

        extractor = UIExtractor()

        elements = (
            extractor.get_settings_elements()
        )

        builder = StateBuilder()

        state = builder.build(elements)

        return state