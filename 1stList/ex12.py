#Considering someone's statue, make a programm able to calculate the ideal weight from the person.
#   Use this formula: (72.7 * altura) - 58

statue = float(input("Inform someone's statue: "))
ideal_weight = (statue * 72.7) - 58

print(f'A {statue}cm person shall weight {ideal_weight} kilos')
