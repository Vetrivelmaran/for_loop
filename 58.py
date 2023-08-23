"""Write a program to find the sum of first and last digit of a number.
Sample Output:
Input any number: 12345
The first digit of 12345 is: 1
The last digit of 12345 is: 5
The sum of first and last digit of 12345 is: 6"""
n=int(input('enter ->'))
s=str(n)
sum =int(s[0])+int(s[-1])
print(f'sum of firs digit anf last difit {sum}')
