#Make a programm that asks how much you earn by a hour and how many hours per month you work.

earn_hour = int(input('Type how much you earn in one hour: '))
hours_month = int(input('Type how many hours you work in one mounth: '))

wage = earn_hour * hours_month

print(f'Your wage is {wage}$')

