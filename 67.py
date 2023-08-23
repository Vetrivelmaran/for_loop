"""Write a program to convert a decimal number to binary number."""
n=7
while n!=0:
    rem =n%2
    print(rem,end='')
    n//=2
