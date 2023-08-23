#Find the smallest prime factor of a given number.
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
n=int(input('entr'))
for j in range(1,n+1):
     if n%j==0:   
        if prime(j):
            print(j)
            break
            
        
        
            

        
            
            