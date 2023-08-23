"""62. Write a program to find power of any number using for loop.
Sample Output:
Input the base: 2
Input the exponent: 5
2 ^ 5 = 32"""
base =int(input('enter-->'))
e =int(input('enter-->'))
pov=1
for i in range(e):
    pov =pov*base
print(pov)