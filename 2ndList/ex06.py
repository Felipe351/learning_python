#Make a programm that reads 3 numbers and them prints the higher value.

first = float(input('First number: '))
second = float(input('Second number: '))
third = float(input('Third number: '))

if first > second and first > third:
  print(f'{first} is the higher value.')
elif second > third:
  print(f'{second} is the higher value.')
else:
  print(f'{third} is the higher value.')
