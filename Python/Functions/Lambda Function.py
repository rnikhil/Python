"""
Anonymous / Lambda Function:
============================
In Python, anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword, in Python anonymous functions
are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.
Syntax:
=======
lambda arguments: expression

Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned.
ex:
double = lambda x: x * 2

print(double(5)) -----> o/p is 10.

In the above program, lambda x: x * 2 is the lambda function. Here x is the argument and x * 2
is the expression that gets evaluated and returned.

This function has no name. It returns a function object which is assigned to the identifier double.

Use of Lambda Function:
========================
We use lambda functions when we require a nameless function for a short period of time.

In Python, we generally use it as an argument to a higher-order function (a function that takes in
other functions as arguments). Lambda functions are used along with built-in functions like filter(), map() etc.

example use with filter() function:
====================================
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list) -----> o/p is [4, 6, 8, 12]

example use with map() function:
================================
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)  --------> o/p is [2, 10, 8, 12, 16, 22, 6, 24]
"""