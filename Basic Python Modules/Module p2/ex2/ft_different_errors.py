def garden_operations(operation_number: int) -> None:

    '''haults when finds error sends back to "try-except" '''
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "Python" + 42
    else:
        return


def test_error_types() -> None:
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")

        try:
            garden_operations(operation_number)
        except ValueError as msg:
            print(f"Caught ValueError: {msg}")
        except ZeroDivisionError as msg:
            print(f"Caught ZeroDivisionError: {msg}")
        except FileNotFoundError as msg:
            print(f"Caught {FileNotFoundError}: {msg}")
        except TypeError as msg:
            print(f"Caught TypeError: {msg}")
        else:
            print("Operation completed successfully")
            print("\n")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
