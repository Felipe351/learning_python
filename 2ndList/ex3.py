#Make a programm that read a letter typed, if it's 'f' then print 'Female', if it's 'm' then print 'male', if it's something else it may print 'Invalid Sex'.

letter = input("Type 'f' for Female 'm' for Male: ")

if not letter == 'm' or letter == 'M':
  if letter == 'f' or letter == 'F':
    print('Female')
  else:
    print('Invalid Sex')
else:
  print('Male')
