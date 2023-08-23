"""Write a program to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....]."""
import math

x=3;n=5;sum=0
for i in range(1,n+1):
    sum+=(x**i/math.factorial(i))
print(sum)