n=[5,9,4,8,2]
f=[]
for i in n:
    fact=1
    for j in range(1,i+1):
        fact*=j
    f.append(fact)
print(f)
    
        