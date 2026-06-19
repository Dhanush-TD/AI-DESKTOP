import uiautomation as auto

settings_window = auto.WindowControl(
    searchDepth=1,
    Name="Settings"
)

if not settings_window.Exists(3):
    print("Settings window not found")
    exit()

print("\nSearching Bluetooth controls...\n")

for control, depth in auto.WalkControl(
    settings_window,
    maxDepth=20
):

    try:

        if "bluetooth" in control.Name.lower():

            rect = control.BoundingRectangle

            print(
                f"Name={control.Name}"
            )

            print(
                f"Type={control.ControlTypeName}"
            )

            print(
                f"Rect=({rect.left}, {rect.top}, "
                f"{rect.right}, {rect.bottom})"
            )

            print("-" * 50)

    except Exception:
        pass