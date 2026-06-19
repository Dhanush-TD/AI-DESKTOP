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

from adapters.desktop.coordinate_resolver import (
    CoordinateResolver
)

resolver = CoordinateResolver()

coords = resolver.find_element_center(
    "Bluetooth & devices"
)

print(
    "\nCoordinates:\n"
)

print(coords)