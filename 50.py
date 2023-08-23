"""Write a program to Check Whether a Number can be Express as Sum of
Two Prime Numbers.
Sample Output:
Input a positive integer: 20
20 = 3 + 17
20 = 7 + 13"""

def isPrime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
n=5
for i in range(1,(n//2)+1):
    p=n-i
    if isPrime(p) and isPrime(i):
        print(p,i)
        







