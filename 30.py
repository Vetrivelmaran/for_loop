"""Write a program to find the last prime number occur before the entered
number."""
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
for j in range(50,1,-1):
    if prime(j):
        print(j)
        break