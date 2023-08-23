#Write a program to convert a binary number to decimal number.
n=1011
i=0
som=0
while n!=0:
    rem=n%10
    som +=rem*(2**i)
    i+=1
    n=n//10
    
print(som)
    

