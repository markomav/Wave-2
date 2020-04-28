from random import randrange

random_value = randrange(0, 37+1)

print("The spin landed on " + random_value, "...")

if not random_value or random_value == 37:
    print('Pay None')
elif random_value % 2 and (random_value >= 1 and random_value <= 9)
    print('Pay Red')
else:
    print('Pay Black')

if not random_value or not (random_value == 37):
    if random_value % 2:
        print('Pay Odd')
    else:
        print('Pay Even')

if random_value >= 1 and random_value <= 18:
    print('Pay 1 to 18')
elif random_value >= 19 and random_value <= 36:
    print('Pay 19 to 36')