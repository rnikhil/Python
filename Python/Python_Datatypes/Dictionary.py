"""
Dictionary:
===========
Dictionary is unordered collection of (key,value) pair.
Dictionary is used when we have huge amount of data.
Dictionaar is defined with braces {} with each item being a pair in form of key:value.
we can use key to retrieve the respective value.
ex:
---
dict = {'name':'nikhil', 'age':25}

Accessing elements of  a dictionary:
====================================
We can use keys with in square brackets or get() to access elements of a dictionary.
but when we use get() it returns 'None' if there is no key instead of 'key error'
ex:
---
dict = {'name':'nikhil', 'age':25}
print(dict['name'])  ---> o/p is nikhil.
ex:
---
dict = {'name':'nikhil', 'age':25}
print(dict.get('age'))  ---> o/p is 25.

Change or Add elements to a Dictionary:
=======================================
we use assignment operator to change or add element in a dictionary.If key is already present
value gets updated else new (key:value) pair is added to the dictionary.
ex:
---
dict = {'name':'nikhil', 'age':25}
dict['age'] = 26
print(dict)  ----> o/p is {'age': 26, 'name': 'nikhil'}

ex:
---
dict = {'name':'nikhil', 'age':25}
dict['address'] = 'Dallas'
print(dict)  -----> o/p is {'name': 'nikhil', 'age': 25, 'address': 'Dallas'}

Delete or Remove Element from the Dictionary:
==============================================
pop():
=====
we can remove particular item uisng pop() mehtod. This method removes an item with the provided key and
returns the value.
ex:
---
squares = {2:4,3:9,4:16,5:25}
print(squares.pop(4)) ----> o/p is 16.

popitem():
=========
It is used to remove and return an arbitrary item (key,value)
ex:
---
squares = {2:4,3:9,4:16,5:25}
print(squares.popitem()) ----> o/p is (2, 4)

clear():
=======
All items can be removed atonce using clear() method.
ex:
---
squares = {2:4,3:9,4:16,5:25}
squares.clear()
print(squares) ----> o/p is {}

del:
====
we can also use 'del' keyword to remove individual item or the entire dictionary.
ex:
----
squares = {2:4,3:9,4:16,5:25}
del squares[5]
print(squares) ----> o/p is {2: 4, 3: 9, 4: 16}

Built in Functions in dictionary:
=================================
1. all() - Returns True if all the keys of the dictionary are True (or) if the dictionary is empty.
2. any() - Returns True if any key of the ditionary is True , if the dictionary is empty returns False.
3. len() - Returns the length.
4. cmp() - Compares items of two dictionaries.
5. sorted() - Returns a new sorted list of keys in the dictionary.

Iterating through dictionary:
=============================
Using for loop we can iterate through each key in a dictionary.
ex:
---
squares = {2:4,3:9,4:16,5:25}
for i in squares:
    print(squares[i])

Membership Test:
================
we can test if akey is in a dictionary or not using 'in' Keyword.
In a dictionary we can only test for presence of key, not the value.
ex:
squares = {2:4,3:9,4:16,5:25}
print(2 in squares) ----> o/p is True.

Dictionary Methods:
===================

"""