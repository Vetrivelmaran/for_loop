"""59. Write a program to find the frequency of each digit in a given integer.
Sample Output:
Input any number: 122345
The frequency of 0 = 0
The frequency of 1 = 1
The frequency of 2 = 2
The frequency of 3 = 1
The frequency of 4 = 1
The frequency of 5 = 1
The frequency of 6 = 0
The frequency of 7 = 0
The frequency of 8 = 0
The frequency of 9 = 0"""
n=int(input('enter the number'))
s =str(n)
for i in range(11):
    print(f'the freqency of {i}',s.count(str(i)))
    