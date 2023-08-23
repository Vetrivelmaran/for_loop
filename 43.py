"""Write a program to find the sum of the series [ x - x^3 + x^5 + ......]."""
x=2;n=5;sum=0
for i in range(1,n+1,2):
    sum+=x**i
print(sum)