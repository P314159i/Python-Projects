def ft_garden_intro() -> None:
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


def main() -> None:
    print("=== Welcome to My Garden ===")
    ft_garden_intro()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
