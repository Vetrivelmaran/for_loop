"""Write a program to calculate product of digits of any number.
Sample Output:
Input a number: 3456
The product of digits of 3456 is: 360"""
n=int(input('enter ->'))
product=1
for i in str(n):
    product =product*int(i)
print(f'product of firs digit anf last difit {product}')