"""Write a program to make such a pattern like right angle triangle with number
increased by 1."""
k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=' ')
        k+=1
    print( )
    
#1 
#2 3 
#4 5 6 
#7 8 9 10 