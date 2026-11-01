print("uloha4")
sucet = 0
pocet = 0
cislo = int(input("zadaj cislo:"))
while cislo != 0:
    sucet += cislo
    pocet += 1
    cislo = int(input("zadaj cislo:"))
print("priemer je:", sucet / pocet)




print("uloha5")
pocet = 0
slovo = input("zadaj slovo:")
while slovo[0] != "x":
    pocet += len(slovo)
    slovo = input("zadaj slovo:")
print("pocet znakov:", pocet)