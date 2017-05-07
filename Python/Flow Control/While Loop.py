"""
while loop:
===========
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
We generally use this loop when we don't know beforehand, the number of times to iterate.
Syntax:
=======
while test_expression:
    Body of while

ex:
n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter
# print the sum
print("The sum is", sum)

while loop with else:
=====================
Same as that of for loop, we can have an optional else block with while loop as well.
The else part is executed if the condition in the while loop evaluates to False. The while loop can be terminated
with a break statement.
In such case, the else part is ignored. Hence, a while loop's else part runs if no break occurs
and the condition is false.

ex:
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
    
"""

