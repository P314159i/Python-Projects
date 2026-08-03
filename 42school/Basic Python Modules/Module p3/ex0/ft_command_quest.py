import sys


def main() -> None:
    print(f"Program name: {sys.argv[0]}")
    if (sys.argv > 0):
        print(len(sys.argv))
        for ()
    else:
        print("No arguments provided!")

main()


## Exercise 0: Command Quest

The subject wants you to:

* Create `ft_command_quest.py`.
* Import `sys`.
* Read command-line arguments from `sys.argv`.
* Print the program name.
* If no extra arguments were given, print `No arguments provided!`
* Otherwise:

  * print how many arguments were received;
  * print each argument with its number, starting from `1`.
* Print the total number of items in `sys.argv`, including the program name.
* Match the example output format.
* Avoid printing the program name again as a normal argument.
* Use only `import sys`, `sys.argv`, `len()`, and `print()`. 
