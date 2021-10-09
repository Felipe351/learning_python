#Make a programm that asks for a number and inform if it's a positive ou negative number.

number = float(input('Type a number: '))

if number == 0:
  print("0 is a neutral number, not positive, nor negative")
elif number > 0:
  print(f'{number} is a positive number')
else:
  print(f'{number} is a negative number')
