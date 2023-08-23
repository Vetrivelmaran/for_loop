"""Write a program to find the Sum of GP series.
Sample Output:
Input the starting number of the G.P. series: 3
Input the number of items for the G.P. series: 5
Input the common ratio of G.P. series: 2
The numbers for the G.P. series:
3 6 12 24 48
The Sum of the G.P. series: 93"""

n=5
d=3
som=0
for i in range(1,n+1):
    som=som+d
    d=d*2
print(som)