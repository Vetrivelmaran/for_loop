#Write a program to display the first n terms of Fibonacci series
n=int(input('enter ->'))
a=0;b=1
for i in range(n+1):
    print(a)
    a=a+b
    a,b=b,a