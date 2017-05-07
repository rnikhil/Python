"""
Numbers:
========
Integers, float, Complex numbers all together form a number category. They are defined as
int, float, complex class in python.

Type():
=======
type() function is used to know to which class a variable or value belongs to.
ex:
a = 5
print(type(a))

isinstance():
=============
isinstance() function is used to check if an object belongs to a particular class or not
ex:
a = 5
print(isinstance(5, 'int'))

Integers:
=========
They are numeric data types (+ve or -ve). If compatible you can convert an integer to any data type by placing the
data type you want to convert before the value or variable.
ex:
a = str(20)
print(type(a))

bases:
======
base2(b) ---> 0 and 1
base8(o) ---> 0 to 7
base10 ---> usual numeric system
base16(x) ---> 0 to 9 and A to F

converting numeric base to other bases:
=======================================
we use bin() --> to convert it to binary base or base2
we use oct() --> to convert it to base8
we use hex() --> to convert it to base16

ex:
t = 100
bin(t)

Float:
======
Numbers with decimal points are called floating point numbers. A float is accurate up to 15 decimal points.
round() is a function which is used only with floating point numbers.
ex: 5 and 5.0 are different in python ('5' is an integer whereas '5.0' is a float)
ex:
round(4.3)
4.0
ex:
round(4.6)
5.0

Complex numbers:
================
Complex numbers are written in x+yj form (where x-> is real part and y-> is imaginary part)
ex:
test = 3+5j
test.real --> It prints only the real part.
test.imag --> It prints only the imaginary part.


"""