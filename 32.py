"""Write a program to find the sum of the series 1 + 1/2^2 + 1/3^3 + ..+ 1/n^n"""
sum=0
n=int(input('enter  ->'))
for i in range(1,n):
    sum +=1/(i**i)
print(sum)    