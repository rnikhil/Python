"""
Special Operators:
==================
Python language offers some special type of operators like the
1. Identity operator
2. Membership operator.

1. Identity Operator (is, is not):
==================================
is and is not are the identity operators in Python. They are used to check if two values (or variables) are
located on the same part of the memory. Two variables that are equal does not imply that they are identical.
ex:
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1) ----> # Output: False

print(x2 is y2) ----> # Output: True

print(x3 is y3) ----> # Output: False

Here, we see that x1 and y1 are integers of same values, so they are equal as well as identical.
Same is the case with x2 and y2 (strings).

But x3 and y3 are list. They are equal but not identical. Since list are mutable (can be changed),
interpreter locates them separately in memory although they are equal.

2. Membership Operator(in, not in):
===================================
in and not in are the membership operators in Python. They are used to test whether a value or variable is
found in a sequence (string, list, tuple, set and dictionary).

In a dictionary we can only test for presence of key, not the value.
ex:
x = 'Hello World'
print('H' in x) -----> o/p is True.
"""

