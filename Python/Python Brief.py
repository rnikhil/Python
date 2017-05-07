"""
Python is a object oriented, High Level programming and scripting language.
Python is an interpreted language.
Python is a "Case-Sensitive" Language

Interpreted language:
---------------------
It is the language where the source code is not compiled before executing the program.
where as in other programming language like java the source code is compiled and creates a .class before executing it.

object oriented language:
-------------------------
It is where the code is encapsulated (contained) within the objects.

High Level Language:
--------------------
It means we can write programs that are more or less independent of particular type of computer.

Scripting Language:
They are precompiled and their execution environment is one that is interpreted.

History:
--------
Python was developed by "GUIDO VAN ROSSUM" in late 80's and 90's
Python is derived from many languages like C, C++, Algol60, UnixShell, Small Talk, ABC, etc.

Running Python:
---------------
After installing and Configuring your desired version of python we can run python in 4 ways:
1. open command prompt in your computer and type python and hit enter and you will see a python shell which tells
that python is installed on your pc.
2. open the inbuilt python command prompt which is available when you install python.
3. open the inbuilt python IDLE (Integrated Development Learning Environment), which is available when you install python.
4. Go to the folder where you have installed python (ex: "C:\Python34\python.exe")and click on python.exe.

Editors for Python:
-------------------
1. Eclipse(Pydev) IDE
2. Juypter IDE
3. Pycharm IDE
4. Notepad++
5. sublime text

PIP:
---
PIP (pip install python or pip install package) is  a software management system, which is used to install
and manage third party libraries.

Package:
--------
It is a collection of modules

Module:
-------
It is prewritten code, which is written by someone else.

Naming Convention:
------------------
1. The name of the class must start with Capital letter.
2. variable name can start with letters(upper or lower), _(underscore)
followed by Zero or more letters, underscores or digits(0 to 9)
3. They should have special charcters ($,%,!,@,%)
4. Keywords cannot be used as identifiers.

Indentifiers:
-------------
Names which are used to identify variables, functions, Class, module, etc.

Keywords:
---------
Keywords are also known as Reserved words, They cannot be used as a constant or variable name.

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']

we can see what are the keywords that are present in python using:
------------------------------------------------------------------
import keyword
print(keyword.kwlist)

Indentation:
------------
In other languages like java etc. we use paranthesis to place bolck of code. But in python we use indentation for
a block of code.
ex:
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

Line Continuation Character(\):
-------------------------------
It denotes that line should be continued. Statements within [],{},() does not need to use line continuation character.

Comments:
--------
It describes what is going on in the program. so, that the person looking for the first time deos not have hard time in
understanding it.
There are 2 types of comments:
1. Single Line Comments:
# This is a single line Comment
2. Multi-Line Comments:
"""
"""
This is a
multi-line
Comment
"""
"""
Variables:
==========
They are used to store data. The assignment operator(=) is used to assign value to a variable.
we can reassign variables

Multiple Assignment:
===================
we can make multiple assignments in one statement.
ex: a,b,c = 5,2.5,'hello'
we can assign same values to multiple variables at once.
ex: a = b = c = 'hello'

Conversion between datatypes:
=============================
we can convert one datatype to other using type conversion functions like int(), str(), float().

sep:
====
Separator is used between the values. The default separator is space character.
ex:
print(1,2,3,4, sep = '#')  ----> o/p is 1#2#3#4

end:
====
Its default is a new line, After all values end is printed.
ex:
print(1,2,3,4, end = '&') ----> o/p is 1 2 3 4&

Output Formatting:
==================
we use output formatting to make it look attractive. This can be done using str.format() method.
ex:
x = 5 , y = 10
print('the value of x is {} and y is {}' .format(x,y) -----> o/p is the value of x is 5 and y is 10

we can use keyword arguments:
ex:
print('hello {name},{greetings}' .format(greetings = 'good morning', name = 'nikhil')) ---> o/p is hello nikhil,good morning

Python import:
==============
If our program grows bigger it is better to break the program into different modules.
A module is a file containing python definition and statements.
Definitions inside a module can be imported using import keyword.
ex:
import math
we can import some specific attributes and functions only using the 'from' keyword
ex:
from math import pi
while importing a module, python looks at different places defined in sys.path
"""