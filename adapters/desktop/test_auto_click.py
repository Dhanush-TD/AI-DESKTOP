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

from adapters.desktop.click_executor import (
    ClickExecutor
)

resolver = CoordinateResolver()

executor = ClickExecutor()

coords = resolver.find_element_center(
    "Bluetooth & devices"
)

print("\nCoordinates Found:\n")
print(coords)

if coords:

    input(
        "\nPress ENTER to auto-click..."
    )

    executor.click(
        coords[0],
        coords[1]
    )

    print(
        "\nClick Executed"
    )

else:

    print(
        "\nElement Not Found"
    )