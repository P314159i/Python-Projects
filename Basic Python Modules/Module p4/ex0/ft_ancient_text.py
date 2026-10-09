import sys
import typing

argv: list[str] = sys.argv


def ft_ancient_text() -> None:

    try:
        argv[1]
    except IndexError:
        print("Usage: ft_ancient_text.py <file>")
        return

    try:

        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{argv[1]}'")
        file: typing.IO[str] = open(argv[1])
        content = file.read()

        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")

        file.close()

        print(f"File '{argv[1]}' closed.")

    except FileNotFoundError as err:
        print(f"Error opening file '{argv[1]}': {err}")
    except PermissionError as err:
        print(f"Error opening file '{argv[1]}': {err}")


def main() -> None:
    ft_ancient_text()


if __name__ == "__main__":
    main()
