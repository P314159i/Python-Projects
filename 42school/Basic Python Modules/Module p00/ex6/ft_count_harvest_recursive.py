def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count_day(day: int) -> None:
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count_day(day + 1)
    count_day(1)


''' def ft_count_harvest_recursive(day=1, days=None):
    if days is None:
        days = int(input("Days until harvest: "))
    if day > days:
        print("Harvest time!")
        return
    print("Day", day)
    ft_count_harvest_recursive(day + 1, days)'''
