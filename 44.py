#Write a program to find the sum of the series 1 +11 + 111 + 1111 + .. n
#terms.

k=1
sum=0
add=0
for i in range(1,6):
    sum=sum*10+k
    add=add+sum
    print(sum,end='+')
print()
print(add)