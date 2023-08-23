"""Write a program to find the Greatest Common Divisor (GCD) of two numbers.
Sample Output"""
n1=int(input('enter ->'))
n2=int(input('enter ->'))
min=n1
if n1>n2:
    min=n2
for i in range(min,0,-1):
    if n1%i==0 and n2%i==0:
        gcd =i
        break
print(gcd)   