"""Write a program to print all ASCII character with their values.
Sample Output:
Input the starting value for ASCII characters: 65
Input the ending value for ASCII characters: 75
The ASCII characters:"""
for i in range(65,76):
    print(f'{i}-->{chr(i)}')