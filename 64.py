"""Write a program to enter any number and print all factors of the number.
Sample Output:
Input a number: 63
The factors are: 1 3 7 9 21 63"""
for i in range(1,63+1):
    if 63%i==0:
        print(i,end=' ')
    