import os
import sys
import site


def check_matrix_stats() -> None:

    if sys.prefix != sys.base_prefix:
        print("\n𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃MATRIX STATUS: Welcome to the construct𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃")
        print(f"\n 📍 Current Python in: \n  {sys.executable}")
        print(f"\n   🤖 Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"\n   ⏣  Environment Path: {sys.prefix}")
        print("\n   ˖ִ🛸  SUCCESS: You're in an isolated environment!")
        print("        Safe to install packages", end="")
        print("        without affecting the global system")
        print("\n    ⏻ Package installation", end="")
        print("        path is in your virtual environment:")
        print(f"    {site.getsitepackages()[0]}")
        print("\n")

    else:
        print("\n𝄃𝄃𝄂𝄃𝄂𝄂𝄃MATRIX STATUS: You're still plugged in𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄀𝄁𝄃𝄂𝄂𝄃")
        print(f"\n   Current Python in: {sys.executable}")
        print("\n   Virtual Environment: None detected!")
        print("\n   📍WARNING: You're in the global environment")
        print("\n      📺 The machines can see everything you install...")
        print("\n   To enter the construct, run:")
        print("      ⚙️  python -m venv matrix_env")
        print("      ⚙️  source matrix_env/bin/activate # On Unix")
        print(r"      ⚙️  matrix_env\Scripts\activate # On Windows")
        print("\n   Then run this program again.\n")


def main() -> None:
    check_matrix_stats()


if __name__ == "__main__":
    main()
