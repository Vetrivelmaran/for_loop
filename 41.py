"""Write a program to display the sum of the series [ 9 + 99 + 999 + 9999 ...]."""
k=9
sum=0
add=0
for i in range(1,6):
    sum=sum*10+k
    add=add+sum
    print(sum,end='+')
print()
print('sum of 9+99+999..',add)