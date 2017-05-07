"""
The if…elif…else statement is used in Python for decision making.
if statement:
=============
syntax:
=======
if test expression:
    statement(s)

Here, the program evaluates the test expression and will execute statement(s) only if the text expression is True.
If the text expression is False, the statement(s) is not executed.

ex:
num = 3
if num > 0:
    print(num, "is a positive number.") ---> o/p is 3 is a positive number.

if else statement:
==================
syntax:
=======
if test expression:
    Body of if
else:
    Body of else

If the condition for if is False, it checks the condition of the next elif block and so on.
If all the conditions are False, body of else is executed.
Only one block among the several if...elif...else blocks is executed according to the condition.
The if block can have only one else block. But it can have multiple elif blocks.

ex:
num = 3.4
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")  ---> o/p is positive number.

Nested if statement:
====================
We can have a if...elif...else statement inside another if...elif...else statement.
This is called nesting in computer programming.

"""