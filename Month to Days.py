month = input('Month: ')

thirty_days = ['april','june','september','november']
thirty_one_days = ['january','march','may','july','august','october','december']

if str.lower(month) == 'february':
    print(month , 'has 28 or 29 days')
elif str.lower(month) in thirty_days:
    print(month , 'has 30 days')
elif str.lower(month) in thirty_one_days:
    print(month , 'has 31 days')
else:
    print('Error: Invalid month')