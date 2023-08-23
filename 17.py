#Find the second smallest element in an array.
a=[2,6,54,7,84,]
min=a[0]
for i in range(len(a)):
    if min>a[i]:
        min=a[i]
print(min)