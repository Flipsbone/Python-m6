#!/usr/bin/env python3

def package_access():
    import alchemy.transmutation
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


def relative_imports():
    import alchemy.transmutation.advanced
    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone(): "
          f"{alchemy.transmutation.advanced.philosophers_stone()}")
    print("elixir_of_life(): "
          f"{alchemy.transmutation.advanced.elixir_of_life()}")


def absolute_imports() -> None:
    import alchemy.transmutation.basic
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}")


def main() -> None:
    print("=== Pathway Debate Mastery ===")
    try:
        absolute_imports()
        relative_imports()
        package_access()
    except (AttributeError, ImportError) as e:
        print(f"{e}")
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
