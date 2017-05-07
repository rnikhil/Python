"""
function arguments:
====================
In user-defined function topic, we learned about defining a function and calling it. Otherwise,
the function call will result into an error.
ex:
def greet(name,msg):
   print("Hello",name + ', ' + msg)

greet("Monica","Good morning!")

Variable Function Arguments:
============================
Up until now functions had fixed number of arguments. In Python there are other ways to define a function
which can take variable number of arguments.

Three different forms of this type are described below.
1. Python Default Arguments
2. Python Keyword Arguments
3. Python Arbitrary Arguments

1. Python Default Arguments:
=============================
Function arguments can have default values in Python.
We can provide a default value to an argument by using the assignment operator (=).
ex:
def greet(name, msg = "Good morning!"):
    print("Hello",name + ', ' + msg)

greet("Kate")  ------> o/p is Hello Kate, Good morning!
greet("Bruce","How do you do?") -----> o/p is Hello Bruce, How do you do?

In this function, the parameter name does not have a default value and is required (mandatory) during a call.

On the other hand, the parameter msg has a default value of "Good morning!". So, it is optional during a call.
If a value is provided, it will overwrite the default value.
Any number of arguments in a function can have a default value. But once we have a default argument,
all the arguments to its right must also have default values.

2. Python Keyword Arguments:
=============================
When we call a function with some values, these values get assigned to the arguments according to their position.

For example, in the above function greet(), when we called it as greet("Bruce","How do you do?"),
the value "Bruce" gets assigned to the argument name and similarly "How do you do?" to msg.

Python allows functions to be called using keyword arguments. When we call functions in this way,
the order (position) of the arguments can be changed.
>>># 2 keyword arguments
>>> greet(name = "Bruce",msg = "How do you do?")

>>> # 2 keyword arguments (out of order)
>>> greet(msg = "How do you do?",name = "Bruce")

>>> # 1 positional, 1 keyword argument
>>> greet("Bruce",msg = "How do you do?")

But we must keep in mind that keyword arguments must follow positional arguments.

3. Python Arbitrary Arguments:
==============================
Sometimes, we do not know in advance the number of arguments that will be passed into a function.Python allows us
to handle this kind of situation through function calls with arbitrary number of arguments.

In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument.
ex:
def greet(*names):
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")
"""