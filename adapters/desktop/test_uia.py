from uia_extractor import UIExtractor


extractor = UIExtractor()

elements = extractor.get_settings_elements()
print(f"\nTotal Elements: {len(elements)}\n")

for e in elements[:100]:

    print(
        f"Name={e.name} | "
        f"Type={e.control_type} | "
        f"Class={e.class_name}"
    )