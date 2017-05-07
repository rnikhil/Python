"""
for loop:
=========
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
Syntax:
=======
for val in sequence:
    Body of for

Here, val is the variable that takes the value of the item inside the sequence on each iteration.

ex:
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0

for val in numbers:
    sum = sum+val

print("The sum is", sum)  ---> Output: The sum is 48

range() function:
==================
We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).
We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.
To make this function to output all the items, we can use the function list().

ex:
print(range(10)) ---> o/p is range(0, 10)

print(list(range(10))) ----> O/p is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

We can use the range() function in for loops to iterate through a sequence of numbers. It can be combined with the
len() function to iterate though a sequence using indexing.
ex:
# Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])  ----> o/p is I like pop
                                            I like rock
                                            ​I like jazz

for loop with else:
===================
A for loop can have an optional else block as well. The else part is executed if the items in the sequence
used in for loop exhausts.
break statement can be used to stop a for loop. In such case, the else part is ignored.
Hence, a for loop's else part runs if no break occurs.

ex:
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")  
"""