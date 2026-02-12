import alchemy


def main() -> None:

    print("=== Sacred Scroll Mastery ===\n")
    try:
        print("Testing direct module access:")
        fire = alchemy.elements.create_fire()
        print(f"alchemy.elements.create_fire(): {fire}")
        water = alchemy.elements.create_water()
        print(f"alchemy.elements.create_water(): {water}")
        earth = alchemy.elements.create_earth()
        print(f"alchemy.elements.create_earth(): {earth}")
        air = alchemy.elements.create_air()
        print(f"alchemy.elements.create_air(): {air}")
    except AttributeError as e:
        print(f"{e}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        fire = alchemy.create_fire()
        print(f"alchemy.create_fire(): {fire}")
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")

    try:
        water = alchemy.create_water()
        print(f"alchemy.create_water(): {water}")
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        earth = alchemy.create_earth()
        print(f"alchemy.create_earth(): {earth}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        air = alchemy.create_air()
        print(f"alchemy.create_air(): {air}")
    except (AttributeError, ImportError):
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")

    try:
        print(f"Version: {alchemy.__version__}")
    except AttributeError:
        print("Version: Not defined")

    try:
        print(f"Author: {alchemy.__author__}")
    except AttributeError:
        print("Author: Not defined")


if __name__ == "__main__":
    main()
