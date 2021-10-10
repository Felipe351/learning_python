#Make a programm that reads 3 numbers and prints the higher and the lower value.

first = float(input('Type the first number: '))
second = float(input('Type the second number: '))
third = float(input('Type the last one: '))

if first > second and first > third:
  if second > third:
    print(f'{first} is the higher and {third} is the lower value.')
  else:
    print(f'{first} is the higher and {second} is the lower value.')
elif second > third:
  if first > third:
    print(f'{second} is the higher and {third} is the lower value.')
  else:
    print(f'{second} is the higher and {first} is the lower value.')
elif first > second:
  print(f'{third} is the higher and {second} is the lower value.')
else:
  print(f'{third} is the higher and {first} is the lower value.')

