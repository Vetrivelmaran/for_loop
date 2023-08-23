#Remove all duplicates from a list.
a=[2,5,5,58,8]
n=[]
for i in range(len(a)):
    if a[i] not in n:
        n.append(a[i])
print(n)
        