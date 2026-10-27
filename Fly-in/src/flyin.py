from Parsers.map_parser import MapParser


def main() -> None:
    path = ""

    print("  If you wake up in a house that's full of smoke")
    print("  don't panic")
    print("  call me and I'll tell you a joke\n")

    try:
        parser = MapParser(path)
        parser.parse_drone()
        parser.parse_hub()

        print(parser.num)
        print(parser.start_hub)
        print(parser.end_hub)

    except (ValueError, OSError) as err:
        print(err)


if __name__ == "__main__":
    main()
