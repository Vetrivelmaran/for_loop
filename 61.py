"""60. Write a program to input any number and print it in words.
Sample Output:
Input any number: 8309
Eight Three Zero Nine"""

n=5030
a=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
s=str(n)

for i in range(len(s)):
    for j in range(11):
        if j==int(s[i]):
            print(a[i],end=' ')
    