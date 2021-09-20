#Make a programm that asks two numbers and prints the higher value

first = int(input('Type a number: '))
second = int(input('Type another number: '))

if(first == second):
  print('Both numbers have the same value')
else:
  if(first > second):
    print(f'{first} is the number with the higher value')
  else:
    print(f'{second} is the number with the higher value')
