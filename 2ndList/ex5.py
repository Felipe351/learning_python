firstNote = float(input('Type your first note: '))
secondNote = float(input('Type your second note: '))

average = (firstNote + secondNote) / 2

if average < 7:
  print('Reproved')
elif average == 10:
  print('Aproved with award')
else:
  print('Aproved')
