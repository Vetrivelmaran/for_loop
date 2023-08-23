#Given a list of numbers, find the index of the first occurrence of a given number.
a=[2,4,52,4,2,26,872,2]
n=int(input('enter->'))
for i in range(len(a)):
    if n==a[i]:
        print(i)
        break
