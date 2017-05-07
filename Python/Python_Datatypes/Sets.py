"""
sets:
=====
A set is an unordered collection of items. Every element is unique (no duplicates) and must
be immutable (which cannot be changed).

However, the set itself is mutable. We can add or remove items from it.

Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

How to Create a set:
====================
A set is created by placing all the items (elements) inside curly braces {}, separated by comma or
by using the built-in function set().

It can have any number of items and they may be of different types
(integer, float, tuple, string etc.). But a set cannot have a mutable element,
like list, set or dictionary, as its element.
ex:
my_set = {1, 2, 3}
print(my_set)

# set of mixed data types
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

Creating an empty set is a bit tricky.

Empty curly braces {} will make an empty dictionary in Python.
To make a set without any elements we use the set() function without any argument.
ex:
a = {}
print(type(a))  -----> o/p is <class 'dict'>

a = set()
print(type(a)) -----> o/p is <class 'set'>

How to change set in python:
============================
Sets are mutable. But since they are unordered, indexing have no meaning.

We cannot access or change an element of set using indexing or slicing. Set does not support it.

How to add an element in set:
==============================
add():
======
We can add single element using the add() method.
ex:
my_set = {1,3}
print(my_set) ---> o/p is {1,3}
my_set.add(2)
print(my_set) ----> o/p is {1,2,3}

update():
=========
we can add multiple elements using the update() method.
The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.
ex:
# add multiple elements
my_set.update([2,3,4])
print(my_set) ----> o/p is {1, 2, 3, 4}

# add list and set
my_set.update([4,5], {1,6,8})
print(my_set) ------> o/p is {1, 2, 3, 4, 5, 6, 8}

How to remove element from the set:
====================================
A particular item can be removed from set using methods, discard() and remove().

discard():
==========
A particular item can be removed from set using discard().
while using discard() if the item does not exist in the set, it remains unchanged.

remove():
=========
A particular item can be removed from set using remove().
while using remove() if the item does not exist in the set, remove() will raise an error in such condition.

pop():
======
we can remove and return an item using the pop() method.
Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.
ex:
my_set = set("HelloWorld")
print(my_set)
# pop an element
# Output: random element
print(my_set.pop())

clear():
========
We can remove all items from a set using clear().
ex:
# clear my_set
#Output: set()
my_set.clear()
print(my_set)

set operations:
================
Sets can be used to carry out mathematical set operations like union, intersection,
difference and symmetric difference. We can do this with operators or methods.

set Union:
==========
Union is performed using | operator. Same can be accomplished using the method union().
ex:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print(A | B)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

ex:
>>> A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}

# use union function on B
>>> B.union(A)
{1, 2, 3, 4, 5, 6, 7, 8}

Set Intersection:
=================
Intersection of A and B is a set of elements that are common in both sets.
Intersection is performed using & operator. Same can be accomplished using the method intersection().
ex:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
print(A & B) # Output: {4, 5}

ex:
>>> A.intersection(B)
{4, 5}

# use intersection function on B
>>> B.intersection(A)
{4, 5}


Set Difference:
===============
Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly,
B - A is a set of element in B but not in A.
Difference is performed using - operator. Same can be accomplished using the method difference().
ex:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
print(A - B) # Output: {1, 2, 3}

ex:
>>> A.difference(B)
{1, 2, 3}

Symmetric Difference:
======================
Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().

ex:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
print(A ^ B)  # Output: {1, 2, 3, 6, 7, 8}

ex:
>>> A.symmetric_difference(B)
{1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
>>> B.symmetric_difference(A)
{1, 2, 3, 6, 7, 8}

Set Methods:
=============
Method	                                            Description
add()	                                            Add an element to a set
clear()	                                            Remove all elements form a set
copy()	                                            Return a shallow copy of a set
difference()	                                    Return the difference of two or more sets as a new set
difference_update()	                                Remove all elements of another set from this set
discard()	                                        Remove an element from set if it is a member. (Do nothing if the element is not in set)
intersection()	                                    Return the intersection of two sets as a new set
intersection_update()	                            Update the set with the intersection of itself and another
isdisjoint()	                                    Return True if two sets have a null intersection
issubset()	                                        Return True if another set contains this set
issuperset()	                                    Return True if this set contains another set
pop()	                                            Remove and return an arbitary set element. Raise KeyError if the set is empty
remove()	                                        Remove an element from a set. If the element is not a member, raise a KeyError
symmetric_difference()                              Return the symmetric difference of two sets as a new set
symmetric_difference_update()	                    Update a set with the symmetric difference of itself and another
union()	                                            Return the union of sets in a new set
update()	                                        Update a set with the union of itself and others

Membership Test:
=================
We can test if an item exists in a set or not, using the keyword in

ex:
my_set = set("apple")
print('a' in my_set)

Iteration through set:
=======================
Using a for loop, we can iterate though each item in a set.
ex:
for letter in set("apple"):
    print(letter)

Built-in Functiions:
====================
Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc.
are commonly used with set to perform different tasks.

Frozenset:
==========
Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
While tuples are immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand,
frozensets are hashable and can be used as keys to a dictionary.

Frozensets can be created using the function frozenset().

This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(),
issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.

ex:
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

ex:
>>> A.isdisjoint(B)
False
>>> A.difference(B)
frozenset({1, 2})
>>> A | B
frozenset({1, 2, 3, 4, 5, 6})
"""