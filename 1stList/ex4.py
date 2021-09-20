#Make a programm that asks 4 numbers and them prints the average.

first = float(input('Type a number: '))
second = float(input('Type one more: '))
third = float(input('Again, type a number: '))
fourth = float(input('Now type the last number: '))

average = (first + second + third + fourth) / 4

print(f'The average is {average}')
