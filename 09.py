#Print the reverse of a given string.
str =input("enter->")
new=''
for i in range(len(str)-1,-1,-1):
    new =new+str[i]
print(new)
    