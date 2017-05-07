"""
Bitwise Operators:
==================
Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.
ex:
2 is 10 in binary and 7 is 111.
Bitwise AND(&):
==============
Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
ex:
x = 0000 1010 y = 0000 0100
x & y = 0000 0000

Bitwise OR(|):
==============
ex:
x = 0000 1010 y = 0000 0100
x | y = 0000 1110

Bitwise NOT(~):
===============
ex:
x = 0000 1010
~x = 1111 0101

Bitwise XOR(^):
==============
Bitwise XOR sets the bits in the result to 1 if either, but not both, of the corresponding bits in the two operands is 1.
ex:
x = 0000 1010 y = 0000 0100
x ^ y = 0000 1110

Bitwise Right Shift(>>):
=========================
ex:
x = 0000 1010
x >> 2 = 0000 0010

Bitwise Left Shift(<<):
=======================
ex:
x = 0000 1010
x << 2 = 0010 1000

"""