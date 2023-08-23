"""31. Write a program to find out the sum of an A.P. series.
Sample Output:
Input the starting number of the A.P. series: 1
Input the number of items for the A.P. series: 8
Input the common difference of A.P. series: 5
The Sum of the A.P. series are :
1 + 6 + 11 + 16 + 21 + 26 + 31 + 36 = 148"""


d=1
som=0
for i in range(1,8+1):
    som=som+d
    d=d+5
print(som)