import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    argc = len(sys.argv)

    if (argc == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        i = 1
        while (i < argc):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {argc}")


main()
