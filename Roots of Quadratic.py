import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = b**2 - 4*a*c

if d == 0:
    root1 = float(-b / (2 * a))
    print('There is 1 real root.')
    print(root1)
elif d > 0:
    root1 = float((-b + math.sqrt(d)) / (2 * a))
    root2 = float((-b - math.sqrt(d)) / (2 * a))
    print('There are 2 real roots.')
    print('Roots: ' + str(root1) + ' and ' + str(root2))
else:
    print('There are 0 real roots.')