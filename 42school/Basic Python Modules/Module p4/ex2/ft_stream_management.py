import sys
import typing

argv = sys.argv
argc = len(sys.argv)


def show(myfile: list[str]) -> None:
    sys.stdout.write("---\n\n")

    for line in myfile:
        sys.stdout.write(line + "\n")

    sys.stdout.write("\n---\n")


def ft_stream_management() -> None:
    start_line: int = 0
    string_list: list[str] = []
    string_trnsfrm: list[str] = []

    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{argv[1]}'\n")

    try:
        file: typing.IO[str] = open(argv[1], "r")
        content: str = file.read()
        file.close()
    except FileNotFoundError as err:
        sys.stderr.write(
            f"[STDERR] Error opening file '{argv[1]}': {err}\n"
        )
        return
    except PermissionError as err:
        sys.stderr.write(
            f"[STDERR] Error opening file '{argv[1]}': {err}\n"
        )
        return

    while content.find("\n", start_line) != -1:
        end_line = content.find("\n", start_line)

        string_list.append(content[start_line:end_line])
        string_trnsfrm.append(content[start_line:end_line] + "#")

        start_line = end_line + 1

    string_list.append(content[start_line:])
    string_trnsfrm.append(content[start_line:] + "#")

    show(string_list)

    sys.stdout.write(f"File '{argv[1]}' closed.\n\n")
    sys.stdout.write("Transform data:\n")
    show(string_trnsfrm)

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    new_file: str = sys.stdin.readline().rstrip("\n")

    if new_file == "":
        sys.stdout.write("Not saving data.\n")
        return

    sys.stdout.write(f"Saving data to '{new_file}'\n")
    sys.stdout.flush()

    try:
        file = open(new_file, "w")
        file.write("\n".join(string_trnsfrm))
        file.close()
    except FileNotFoundError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{new_file}': {err}\n")
        sys.stdout.write("Data not saved.\n")
        return
    except PermissionError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{new_file}': {err}\n")
        sys.stdout.write("Data not saved.\n")
        return

    sys.stdout.write(f"Data saved in file '{new_file}'.\n")
    sys.stdout.write(f"File '{new_file}' closed.\n")


def main() -> None:
    if argc != 2:
        sys.stderr.write(f"[STDERR] Usage: {argv[0]} <file>\n")
        return
    ft_stream_management()


if __name__ == "__main__":
    main()
