import sys
import typing

argv = sys.argv
argc = len(sys.argv)


def ft_archive_creation() -> None:

    file: typing.IO[str] = open(argv[1])
    content = file.read()
    index: int = 0
    s: list[str] = []
    string: str = 0
    i: int = 0

    while content.find("\n", index) != -1:
        if content[index:] != "":
            start_line = index
            end_line = content.find("\n", index)
            index = end_line + 1
            s.append(content[start_line: end_line] + "#")
    s.append(content[index:] + "#")

    for i in s[i]:
        string = string + i + "\n"

    print(String)

    file.close()

def main() -> None:
    ft_archive_creation()


if __name__ == "__main__":
    main()
