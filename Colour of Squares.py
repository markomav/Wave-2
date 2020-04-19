first = input('Coordinate: ')
x = list(first)
width = str(x[0])
length = int(x[1])
letters = ['a','b','c','d','e','f','g','h']
for i, letter in enumerate(letters):
    if letter == width:
        width = i+1
if width > 8 or length > 8:
    print('Invalid coordinates')
elif (width + length) % 2 == 1:
    print('White Square')
elif (width + length) % 2 == 0:
    print('Black Square')
else:
    print('Invalid coordinates')