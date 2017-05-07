"""
Lists:
======
It is ordered sequence of items and it is mutable (changeable).
Lists are declared within Brackets [] and items in lists are separated by comma.
In other languages Lists are called Arrays.
ex:
---
my_list = ['audi','benz','alto']

A List can have another list as an item and this is called Nested List.
A list can contain several datatypes.
ex:
---
my_list = ['python',[2,3,6],4.5]

Accessing Elements From a List:
===============================
We can access elements of a list using index and slicing
index:
======
we can use indexing for accessing an item in a list.
ex:
----
       h e l l o
index  0 1 2 3 4 ( From left to right )
my_list = ['hello']
print(my_list[1]) ----> It prints 'e'

Slicing:
=======
we can use slicing for accessing range of items.
ex:
----
my_list = ['NIKHIL']
print(my_list[1:5])

Change or Add Elements to a list:
=================================
Lists are mutable unlike strings or tuples. we can use assignment (=) operator to change an item or range of items.
ex:
---
odd = [1,2,5,7]
odd[1] = 3
print(odd) ----> o/p is [1,3,5,7]

append():
=========
we can add an item to the list using " append()" method it adds items to the end of the list
ex:
---
odd = [1,3,5]
odd.append(7)
print(odd) ---> o/p is [1,3,5,7]

extend():
========
we can add several items to the list using " extend()"
ex:
---
odd = [1,3,5,7]
odd.extend([9,11,13])
print(odd) ---> o/p is [1,3,5,7,9,11,13]

we can use "+" to combine two lists and "*" to repeat a list for given no. of times.
ex:
---
odd = [1,3,5]
print(odd + [7,9,11]) ---> o/p is [1, 3, 5, 7, 9, 11]

ex:
---
print(['re'] * 3)  ---> o/p is ['re', 're', 're']

insert():
=========
we can insert an item at a desired location by using " insert()" method
ex:
---
odd = [1,3]
odd.insert(1,5)
print(odd) ---> o/p is [1, 5, 3]

Delete or Remove Element From a List:
======================================
del:
====
we ca use 'del' keyword to delete one or more items. we can even delete the entire list.
ex:
---
odd = [1,3,5,7]
del odd[1] ---> for del we will be using index
print(odd) ---> o/p is [1,5,7]

remove():
========
we can use remove() method to remove the given item.
ex:
----
odd = [1,3,5,7,9]
odd.remove(3) ---> for remove() we will ve using the value
print(odd) ---> o/p is [1,5,7,9]

pop():
======
With pop() method we can remove an item at the given index.
ex:
---
odd = ['n','i','k','e']
odd.pop(1)
print(odd) ---> o/p is ['n', 'k', 'e']

If you donot provide any argument for pop() it removes the last element.
ex:
---
odd = ['n','i','k','e']
odd.pop()
print(odd) ---> o/p is ['n', 'i', 'k']

If you want to know what has been removed it is better to assign it to a variable

clear():
========
we can also use clear() method to empty a list
ex:
---
odd = [1,3,5]
odd.clear()
print(odd) ---> o/p is []

List Methods:
=============
we can access list methods as list.method()
1. append() - adds items to the end of the list.
2. extend() - adds all elements of the list to the another list.
3. insert() - inserts an item at the desired location.
4. remove() - removes an item from the list.
5. pop() - removes and returns the an element at the given index.
6. clear() - removes all items in the list.
7. index() -returns the index of the first matched item.
8. count() - returns the count of number of items passed as an argument.
9. sort() - sorts items in the list in the ascending order.
10. reverse() - Reverse the order of itrms in the list.
11. copy() - Returns the shallow copy of the list.

In:
===
we can test if an item exist in a list or not using keyword "in"
ex:
---
odd = ['n','i','k','e']
print( 'n' in odd) ---> o/p is True.

Built in Functions in list:
===========================
all() , any() , enumerate() , len() , list() , max() , min() , sorted() , sum()

Iterating through a list:
==========================
Using a for loop we can iterate through each item in a list.
ex:
---
odd = ['apple' , 'mango' , 'banana']
for fruit in odd:
    print(" I like " , fruit) ----> o/p is I like  apple
                                           I like  mango
                                           I like  banana
"""