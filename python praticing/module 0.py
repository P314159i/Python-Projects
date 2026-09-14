from typing import Generator


def ft_plot_area() -> None:
    l = int(input("Enter length: "))
    w = int(input("Enter width: "))
    print(f"Plot area: {l * w}\n")


def ft_garden_name() -> None:

    name = input("enter garden name ")
    print(f"garden: {name}\n"
            "status: Growing well!")

def ft_hello_garden() -> None:
    print("hllo garde")


def ft_plant_age() -> None:
    age = int(input("Enter age in days: "))
    if (age > 60):
        print("Plant ready to harvest")
        return
    print("Plant not yet ready to harvest")



def ft_count_harvest_recursive(numb: int, n: int) -> None:
    if (numb == None):
        n = 0;
        numb: int = int(input("Enter days: "))
    if n <= numb:
        print(n)
        n += 1
        ft_count_harvest_recursive(numb, n)
        
        
def ft_count_harvest_generator(numb: int) -> Generator[int, None, None]:
    n: int = 1
    while n <= numb:
        yield n
        n += 1

def ft_seed_inventory() -> None:
    x, y, z = input().split()
    print(x)


def  ft_garden_intro() -> None:
    while True:
        t: tuple[str, float, int] = input (
                "Enter <name><height><age>: "
                ).split()
        if len(t) == 3:
            break
        else:
            continue

    try:
        n, h, a = str(t[0]), float(t[1]), int(t[2])
    except ValueError as err:
        print(f"fuck 1 off, {err}")
        return
    except TypeError as err:
        print("fuck 2 off, {err}")
        return

    print(f"name = {n}\nheight = {h}\nage = {a}\n")


def ft_garden_data() -> None:
    for _ in range (0, 2):
        ft_garden_intro()


def main() -> None:
    # ft_garden_name()
    # ft_hello_garden()
    # ft_plot_area()
    # ft_plant_age()
    # ft_count_harvest_recursive(None, None)

    # day: int = int(input("Enter name: "))
    # for day in ft_count_harvest_generator(day):
    #     print(day)

    # ft_seed_inventory()
    ft_garden_data()


main()