try:
  x = float("hello")
except ValueError:
  print("The value has wrong format")
except:
  print("Something else went wrong")


  num = "Python"


try:
  print(10 / 0)
except ZeroDivisionError:
  print("Error in calculation")
except:
  print("Something else went wrong")



  >>> try:
...     with open("non_existent_file.txt", "r") as file:
...         content = file.read()
... except FileNotFoundError:
...     print("The file you're trying to access doesn't exist.")
...
The file you're trying to access doesn't exist.


>>> with open("non_existent_file.txt", "r") as file:
...     content = file.read()
...
Traceback (most recent call last):
    ...
FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'


try:
    print(float(num))
except ValueError:
    print("Invalid numeric value.")

    try:
    with open("abc.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")



for i in range(len(b)):
    try:
        print(a[b[i]])  # This will fail when b[i] is a string
    except TypeError:
        print("TypeError: Check list of indices")