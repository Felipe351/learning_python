#Make a programm that read the value of 3 products and them it may recomend the cheaper product.

first = float(input('First product price: '))
second = float(input('Second product price: '))
third = float(input('Third product price: '))

if first < second and first < third:
  print('the first is the cheaper one, buy it now!')
elif second < third:
  print('the second is the cheaper one, buy it now!')
else:
  print('the third is the cheaper one, buy it now!')
