"""Write a program to find one's complement of a binary number.
Sample Output:"""
n1=int(input('enter ->'))
for i in str(n1):
    if int(i)==1:
        print(0,end='')
    else:
        print(1,end='')
        