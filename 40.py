"""Write a program to display the n terms of harmonic series and their sum.
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms"""
sum=0
for i in range(1,6):
    sum+=1/i
print(sum)
