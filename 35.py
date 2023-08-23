"""Write a program to find the sum of series 1 - X^2/2! + X^4/4!-.... upto nth
term."""
import math
x=3
sum=0
for i in range(1,5):
    if i%2==0:
        p =(-1**i)*i/math.factorial(i)
        sum+=x**p
print(sum)



#---------this code had small issue----