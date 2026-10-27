from Parsers.map_parser import MapParser


def main() -> None:
    path = "maps/challenger/01_the_impossible_dream.txt"

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
