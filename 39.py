#Write a program to display the n terms of odd natural number and their sum.
sum=0
for i in range(11):
    if i%2!=0:
        sum=sum+i
print(sum)