"""Write a program to calculate the sum of the series (1*1) + (2*2) + (3*3) +
(4*4) + (5*5) + ... + (n*n)."""
n=5
sum=0
for i in range(1,n+1):
    print(f'{i}*{i}={i*i}')
    sum=sum+(i*i)
print('sum of series is', sum)
    