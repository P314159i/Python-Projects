import sys
import typing

argv = sys.argv
argc = len(sys.argv)


def show(myfile: list[str]) -> None:
    line: str = ""

    print("---\n")
    for line in myfile:
        print(line)
    print("\n---")


def ft_archive_creation() -> None:

    start_line: int = 0
    string_list: list[str] = []
    string_trnsfrm: list[str] = []
    new_file: str = ""

    try:
        file: typing.IO[str] = open(argv[1], "r")
        content = file.read()
        file.close()
    except FileNotFoundError as err:
        print(f"Error opening file '{argv[1]}': {err}")
        return
    except PermissionError as err:
        print(f"Error opening file '{argv[1]}': {err}")
        return

    while content.find("\n", start_line) != -1:

        if content[start_line:] != "":

            end_line = content.find("\n", start_line)

            string_list.append(content[start_line: end_line])
            string_trnsfrm.append(content[start_line: end_line] + "#")

            start_line = end_line + 1

    if content[start_line:] != "":
        string_list.append(content[start_line:])
        string_trnsfrm.append(content[start_line:] + "#")

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{argv[1]}'")
    show(string_list)

    print(f"File '{argv[1]}' closed.\n")
    print("Transform data:")
    show(string_trnsfrm)

    new_file = input("Enter new file name (or empty): ")

    if new_file == "":
        print("Not saving data.")
        return

    try:
        file = open(new_file, "w")
        file.write("\n".join(string_trnsfrm))
        file.close()

    except FileNotFoundError as err:
        print(f"Error opening file '{new_file}': {err}")
        return

    except PermissionError as err:
        print(f"Error opening file '{new_file}': {err}")
        return

    print(f"Saving data to '{new_file}'")
    print(f"Data saved in file '{new_file}'.")


def main() -> None:
    if (argc != 2):
        print(f"Usage: {argv[0]} <file>")
        return
    ft_archive_creation()


if __name__ == "__main__":
    main()
