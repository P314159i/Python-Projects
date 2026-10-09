import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        s = input(
             "Enter new coordinates as floats in format 'x,y,z': "
            )

        if not s:
            print("Invalid syntax")
            continue

        i = s.find(",")
        j = s.find(",", i + 1)

        # anything after 2nd "," will be put in "z" which'll get type-checked
        # if anything other than int, it'll raise ValueError
        # so no need to check again for s.find(",", j + 1)
        # but still, printing "invalud syntax" is preffered
        # against raising ValueError for extra comma (says subject)
        if i == -1 or j == -1 or s.find(",", j + 1) != -1:
            print("Invalid syntax")
            continue

        x_str = s[:i]
        y_str = s[i + 1:j]
        z_str = s[j + 1:]

        try:
            x = float(x_str)
        except ValueError as err:
            print(f"Error on parameter '{x_str}': {err}")
            continue

        try:
            y = float(y_str)
        except ValueError as err:
            print(f"Error on parameter '{y_str}': {err}")
            continue

        try:
            z = float(z_str)
        except ValueError as err:
            print(f"Error on parameter '{z_str}': {err}")
            continue

        return (x, y, z)


def dist(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
        + (z2 - z1) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")

    p1 = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    d1 = round(dist(p1, (0, 0, 0)), 4)
    print(f"Distance to center: {d1}")

    print("Get a second set of coordinates")

    p2 = get_player_pos()

    d2 = round(dist(p2, p1), 4)
    print(f"Distance between the 2 sets of coordinates: {d2}")


if __name__ == "__main__":
    main()
