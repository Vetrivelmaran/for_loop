#Write a program to display the number in reverse order.
a=int(input('entr ->'))
temp=a
rem=0
while a!=0:
    rem=rem*10+a%10
    a=a//10
print(rem)