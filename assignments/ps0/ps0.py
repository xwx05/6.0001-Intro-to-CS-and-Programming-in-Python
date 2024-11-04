# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.

import numpy
x=int(input("Enter number x: "))
y=int(input("Enter number y: "))
res1=x**y;
res2=numpy.log2(x)
print("X**y = ", str(res1))
print("log(x) = ", str(res2))

