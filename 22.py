#Given two lists, find the common elements and store them in a new list.
a=[2,45,5,3,4]
b=[2,4,6,47,8]
n=[]
for i in range(len(a)) :
    for j in range(len(b)):
        if a[i]==b[j]:
            n.append(a[i])
print(n)    