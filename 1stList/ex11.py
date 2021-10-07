#Make a progamm able to read 2 int numbers and 1 real, them calculate it and print:
#	the first's double with the second's half
#	the sum of first's triple with the third one
#	the third cubed

first = int(input('Inform a int number: '))
second = int(input('Inform one more int number: '))
third = int(input('Inform a real number: '))

print(f"	{(first * 2) + (second / 2)} is the first's double + second's half")
print(f"	{(first * 3) + third} is the first's triple + the third number")
print(f'	{(third * third) * third} is the third cubed')
