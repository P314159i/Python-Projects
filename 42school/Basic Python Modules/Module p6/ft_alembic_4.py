ft_alembic_4.py will use import alchemy to access the alchemy module and then
create air. The create_earth() function will not be exposed through the module
interface and raise an exception when called (you can catch the exception or not, this
is only for pedagogical purposes). A mypy error will also raise, again, on purpose.


=== Alembic 4 ===
Accessing the alchemy module using 'import alchemy'
Testing create_air: Air element created
Now show that not all functions can be reached
This will raise an exception!
Testing the hidden create_earth: Traceback (most recent call last):
File "/tmp/Python/module-06/ft_alembic_4.py", line 12, in <module>
print(f"{alchemy.create_earth()}")
^^^^^^^^^^^^^^^^^^^^