"""
Functions:
===========
Function is a group of related statements that perform a specific task.
Functions help break our program into smaller and modular chunks. As our program grows larger and larger,
functions make it more organized and manageable.
Furthermore, it avoids repetition and makes code reusable.
Syntax:
========
def function_name(parameters):
	"""docstring"""
	statement(s)
An optional return statement to return a value from the function.

ex:
def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")

Once we have defined a function, we can call it from another function, program or even the Python prompt.
To call a function we simply type the function name with appropriate parameters.

Docstring:
==========
he first string after the function header is called the docstring and is short for documentation string.
It is used to explain in brief, what a function does.It is optional.
We generally use triple quotes so that docstring can extend up to multiple lines.
This string is available to us as __doc__ attribute of the function.
ex:
print(greet.__doc__) ---> o/p is This function greets to
	                             the person passed into the
	                             name parameter
Return Statement:
=================
The return statement is used to exit a function and go back to the place from where it was called.
Syntax:
=======
return [expression_list]

If there is no expression in the statement or the return statement itself is not present inside a function,
then the function will return the None object.

Scope and Lifetime of Variables:
=================================
Scope of a variable is the portion of a program where the variable is recognized.
Parameters and variables defined inside a function is not visible from outside. Hence, they have a local scope.

Lifetime of a variable is the period throughout which the variable exits in the memory.
The lifetime of variables inside a function is as long as the function executes.

They are destroyed once we return from the function. Hence, a function does not remember the value of a variable
from its previous calls.

Types of Functions:
===================
Basically, we can divide functions into the following two types:

1.Built-in functions - Functions that are built into Python.
2.User-defined functions - Functions defined by the users themselves.
"""