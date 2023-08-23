#Remove all occurrences of a specific element from a list.
a=[2,4,52,4,2,26,872,2]
n=int(input('enter ->'))
n=[i for i in a if i!=n]
print(n)