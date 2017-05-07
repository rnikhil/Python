"""
Python Modules:
===============
Modules refer to a file containing Python statements and definitions.

A file containing Python code, for e.g.: example.py, is called a module and its module name would be example.
We use modules to break down large programs into small manageable and organized files. Furthermore,
modules provide reusability of code.

We can define our most used functions in a module and import it, instead of copying their definitions
into different programs.

Let us create a module. Type the following and save it as example.py.

# Python Module example

def add(a, b):
   result = a + b
   return result
Here, we have defined a function add() inside a module named example. The function takes in
two numbers and returns their sum.

How to import modules in python:
=================================
We use the import keyword to do this.
ex:
>>> import example

Using the module name we can access the function using dot (.) operation. For example:

>>> example.add(4,5.5) ------> o/p is 9.5

import statement:
=================
We can import a module using import statement and access the definitions inside it using
the dot operator as described above.
ex:
import math
print("The value of pi is", math.pi)  ----> o/p is The value of pi is 3.141592653589793

import with renaming:
=====================
We can import a module by renaming it as follows.
ex:
import math as m
print("The value of pi is", m.pi)

from import statement:
======================
We can import specific names form a module without importing the module as a whole. Here is an example.
ex:
from math import pi
print("The value of pi is", pi)

In such case we don't use the dot operator. We could have imported multiple attributes.

import all names:
=================
We can import all names(definitions) form a module using the following construct.
ex:
from math import *
print("The value of pi is", pi)

module search path:
====================
While importing a module, Python looks at several places. Interpreter first looks for a built-in module then (if not found) into a list of directories defined in sys.path. The search is in this order.

1. The current directory.
2. PYTHONPATH (an environment variable with a list of directory).
3. The installation-dependent default directory.

Reloading a module:
====================
The Python interpreter imports a module only once during a session. This makes things more efficient.

Now if our module changed during the course of the program, we would have to reload it.One way to do this is to
restart the interpreter. But this does not help much.

Python provides a neat way of doing this. We can use the reload() function inside the imp module to reload a module.
ex:
>>> import my_module
>>> imp.reload(my_module)

dir() built-in function:
========================
We can use the dir() function to find out names that are defined inside a module.

For example, we have defined a function add() in the module example.
>>> dir(example)

All the names defined in our current namespace can be found out using the dir() function without any arguments.
>>> import math
>>> dir()
"""