#Check if the given number is a palindrome.
n=int(input('enter >'))
temp=n
rem=0
while n!=0:
    rem =rem*10+n%10
    n=n//10
if temp==rem:
    print('palindrom')
else:
    print('not palindrom')
    