"""16. Given a list of words, print the ones that start with a vowel.
"""
a=['bpple','eetri','idea']
count=0
for i in a:
    if i[0]=='a' or i[0]=='e'or i[0]=='i'or i[0]=='o'or i[0]=='u':
        count+=1
print(count)