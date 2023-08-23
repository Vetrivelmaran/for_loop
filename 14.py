"""15. Count the number of negative numbers in a list of integers."""


a=[1,6,-4,8,-6]
count=0
for i in range(len(a)):
    if a[i]<0:
        count +=1
print(count)