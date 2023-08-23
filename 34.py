"""Write a program to calculate the series (1) + (1+2) + (1+2+3) + (1+2+3+4) +
... + (1+2+3+4+...+n)."""
n=5
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum+=j
print(sum)