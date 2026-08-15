import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    inputs: list[str] = sys.argv
    number_of_inputs = len(sys.argv) - 1

    i = 1
    while i <= number_of_inputs:
        sep = inputs[i].find(":")

        if sep == -1:
            print(f"Error - invalid parameter '{inputs[i]}'")
            i += 1
            continue

        name = inputs[i][:sep]

        if name == "":
            print(f"Error - invalid parameter '{inputs[i]}'")
            i += 1
            continue

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            i += 1
            continue

        try:
            qty = int(inputs[i][sep + 1:])
        except ValueError as err:
            print(f"Quantity error for '{name}': {err}")
            i += 1
            continue

        inventory.update({name: qty})
        i += 1

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    i = 0
    while i < len(items):
        if total == 0:
            percentage = 0.0
        else:
            percentage = round(
                inventory[items[i]] / total * 100,
                1
            )

        print(
            f"Item {items[i]} represents "
            f"{percentage}%"
        )
        i += 1

    if len(items) > 0:
        most = items[0]
        least = items[0]

        i = 1
        while i < len(items):
            if inventory[items[i]] > inventory[most]:
                most = items[i]

            if inventory[items[i]] < inventory[least]:
                least = items[i]

            i += 1

        print(
            f"Item most abundant: {most} "
            f"with quantity {inventory[most]}"
        )
        print(
            f"Item least abundant: {least} "
            f"with quantity {inventory[least]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()



Three parts.

### 1. Percentage

If:

```python
inventory = {"sword": 2, "potion": 6}
```

total is `8`.

Sword percentage:

```text
2 / 8 * 100 = 25%
```

So in code:

```python
percentage = round(
    inventory[items[i]] / total * 100,
    1
)
```

`inventory[items[i]]` = quantity of the current item.

---

### 2. Most abundant

Start by assuming the **first item** is the biggest:

```python
most = items[0]
```

Then check every other item:

```python
if inventory[items[i]] > inventory[most]:
    most = items[i]
```

Example:

```text
sword = 2
potion = 6

6 > 2 → most becomes "potion"
```

---

### 3. Least abundant

Same idea:

```python
least = items[0]
```

Then:

```python
if inventory[items[i]] < inventory[least]:
    least = items[i]
```

Important: we use `>` and `<`, **not `>=` or `<=`**, so if two quantities tie, the first item stays selected—exactly what the subject asks. 
