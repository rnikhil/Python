"""
Tuple:
======
Tuple is similar to List but Tuples are immutable (not changeable).
Generally we use Tuples for Heterogeneous datatypes and Lists are used for Homogeneous datatypes.
Tuples are denoted by paranthesis()
ex:
---
odd = (2,'hello',5.5)
if you want to create a tuple with only one item in it we should indicate it with comma after the item
ex:
---
odd = ('python' , )

Accessing Elements in a Tuple:
==============================
Using indexing and Slicing

index:
======
It is used to access an item from a tuple
ex:
---
my_tuple = ('red','orange','green')
print(my_tuple[1]) ---> o/p is 'orange'

Slicing:
========
It is used to access range of items from a tuple.
ex:
---
my_tuple = ('p','y','t','h','o','n')
print(my_tuple[0:]) ---> o/p is ('p', 'y', 't', 'h', 'o', 'n')

Tuples cannot be changed but it tuple Contains a list they can be changed.
ex:
----
my_tuple = (4,5,6,[2,3])
my_tuple[3][0] = 1
print(my_tuple) ---> o/p is (4,5,6,[1,3])

Delete or remove a tuple:
==========================
AS discussed, we can change, delete or remove elements of a tuple.
But we can delete the tuple entirely using 'del' keyword.

Tuple Methods:
==============

index(x):
========
Returns index of the first item equal to x.
ex:
---
my_tuple = ('n','i','k','h','i','l')
print(my_tuple.index('i'))  ----> o/p is 1

count(x):
=========
Returns the number of items that is equal to x.
ex:
---
my_tuple = ('n','i','k','h','i','l')
print(my_tuple.count('i'))  ----> o/p is 2.

Built in Functions:
====================
all(), any(), enumerate(), len(), max(), min(), tuple(), sum(), sorted()

Tuple Membership Test:
======================
in:
===
We can check if an item exist in a tuple or not using 'in'
ex:
---
odd = ('n','i','k')
print('n' in odd) ---> o/p is True.
ex:
---
odd = ('n','i','k')
print('n' not in odd) ---> o/p is False.

Iterating through Tuple:
========================
Using for loop we can iterate through each item in a tuple.
ex:
---
for name in ('john','mike'):
    print("hello",name) ---> o/p is hello john
                                    hello mike.

"""