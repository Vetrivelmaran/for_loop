"""Write code to create a checkerboard pattern with the words "black" and
"white".
Sample Output:
Input number of rows: 5
black-white-black-white-black
white-black-white-black-white
black-white-black-white-black
white-black-white-black-white
black-white-black-white-black"""
a='black'
b='white'
for i in range(5):
    for j in range(5):
        print(a,end=' ')
        a,b=b,a
    print()