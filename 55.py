"""Write a program to print a pattern like highest numbers of columns appear in
first row.
Sample Output:
Input the number of rows: 5
12345
2345
345
45
5"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()
