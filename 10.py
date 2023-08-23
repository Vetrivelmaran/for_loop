#Count the number of vowels in a string.
s =input('enter-> ')
count=0
for i in range(len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        count+=1
print(count)

  