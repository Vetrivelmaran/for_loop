"""Write a program to find prime number within a range.
Input number for starting range: 1"""
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
for j in range(1,101):
    if prime(j):
        print(j,end=' ')