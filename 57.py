"""Write a program to find the first and last digit of a number.
Sample Output:
Input any number: 5679
The first digit of 5679 is: 5
The last digit of 5679 is: 9"""
n=int(input('enter ->'))
s=str(n)
print(f'first digit is {s[0]}')
print(f'last digit is {s[-1]}')