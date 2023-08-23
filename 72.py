"""Write a program to convert a binary number to octal number.
Sample Output:
Input a binary number: 1011
The equivalent octal value of 1011 is : 13"""
n=1011
s=str(n)
dec=int(s,2)
print(oct(dec)[2:])
