"""
String:
=======
It is a sequence of characters. Strings can be executed by enclosing characters in single or double quotes.
Strings are immutable (not changeable) means they cannot be changed once they are assigned.
ex:
test = "this is a string"
print(test)

Concatenation:
==============
Joining two or more strings into one is called concatenation. '+' is used for concatenation
ex:
str1 = 'nik'
str2 = 'hil'
print(str1+str2) ---> This prints 'nikhil'

Indexing:
=========
If you want to access individuals characters we use indexing. Indexing starts from 0 from left to right
and from -1 from right to left.
        N  I  K  H  I  L
Index:  0  1  2  3  4  5  ( From Left to Right)
       -5 -4 -3 -2 -1     ( From Right to Left)
test = " Nikhil"
print(test[0]) --> It prints character 'n'
print(test[1]) --> It prints character 'i'

Slicing:
========
If you want to access range of characters we use slicing,
ex:
test = "NIKHIL"
print(test[0:]) --> It prints characters from index[0] to index[5] ie. NIKHIL
print(test[2:5]) --> It prints 'khi' because here index[2] is inclusive and index[5] is exclusive

delete/change string:
=====================
we cannot change already assigned string or delete characters of a string. But we can delete the entire string using
'del' keyword.

in/not:
=======
we can see if a substring exists within a string or not uisng 'in' and 'not' keywords
ex:
a in program ---> It returns True.
a not in program ---> It returns False.

Built-in Functions:
====================
1. len(): It returns length of the string
str1 = "NIKHIL"
print(len(str1)) --> Its o/p is 6

2. enumerate(): It contains index and value of all items in the stringas pair.
ex:
str1 = "NIKHIL"
print(list(enumerate(str1))) --> it gives o/p as [(0, 'N'), (1, 'I'), (2, 'K'), (3, 'H'), (4, 'I'), (5, 'L')]

3. lower(): It converts the string to lower case.
ex:
str1 = 'NIKHIL'
print(str1.lower()) --> o/p is nikhil

4. upper(): It converts the string to upper case.
ex:
str2 = "chaitu"
print(str.upper()) --> o/p is CHAITU

5. strip(): It is used to strip both leading and trailing spaces.
ex:
str2 = "  chaitu  "
print(str2.strip())

6. split(): It splits the string into List
ex:
str3 = "Hello Nikhil"
print(str3.split()) --> o/p is ['Hello' , 'Nikhil']

7. count(): It gives how many characters are repeated
ex:
str4 = "Hello Chaitu"
print(str4.count('l')) --> o/p is 2

8. swapcase(): It converts the string from upper to lower and lower to upper
ex:
str5 = "Hello"
print(str5.swapcase()) --> o/p is 'hELLO'

RawString:
==========
we can ignore escape characters in a string by using raw string it is denoted by 'r' or 'R' . It should be place
before or infront of the string.
ex:
str = " My name is /n Nikhil
print(str) ---> o/p is MY name is /n Nikhil.

String Formatting:
==================
We use place holders in sring formatting. %s(string), %d(integer), %f(float) are used for string formatting
ex:
str = "nikhil"
print("I am %s",% str) --> o/p is I am nikhil.

But, in python 3.x we will be using fromat() for string fromatting and {} as place holder
ex:
str = "nikhil"
print("I am {}" .format("nikhil")) ----> o/p is I am nikhil

we can also specify which value goes to which braces or place holder using indexno
ex:
v1 = "Name is {1} and age is{0} " .format(25,'nikhil')
print(v1) ---> o/p is Name is nikhil and age is 25.






"""

