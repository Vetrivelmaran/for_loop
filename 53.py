"""Write a program to make such a pattern like right angle triangle using
number which will repeat the number for that row."""
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print( )
    
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5 