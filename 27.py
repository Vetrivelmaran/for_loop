"""Write a program to find the perfect numbers between 1 and 500.
The perfect numbers between 1 to 500 are:"""
for n in range(1,501):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        print(sum)
   
    