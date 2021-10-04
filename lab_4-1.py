# Author MB 09/30/2021

magic_charge = int(input("magic charge: "))

shield_charge = int(input("shield charge: "))

if not((magic_charge >= 90) and (shield_charge >= 75)):
    print("The dragon burns you to a crisp")
else:
    print("Thank you! But our princess is in another castle.")
