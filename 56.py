"""Write a program to print the Floyd's Triangle.
Sample Output:
Input number of rows: 5
1
01
101
0101
10101"""
a=1

for i in range(1,6):
    for j in range(1,i+1):
        if a==1:
            print(1,end='')
            a=0
        else:
            print(0,end='')
            a=1
    print()
    