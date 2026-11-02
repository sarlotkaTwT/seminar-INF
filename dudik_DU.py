print("uloha cislo 1")
n = int(input("Zadaj cislo")) #vypytam si cislo
sucet = 0
while n > 0:
    cifra = n % 10 #zvysok po deleni 10 - posledna cifra cisla
    sucet += cifra
    n //= 10 #celociselne delenie - odstrani poslednu cifru cisla
print(sucet)


print("uloha cislo 2")
n=int(input("Zadaj cislo"))
pocet = 0
while n > 0:
    cifra = n % 10 #zvysok po deleni 10 - posledna cifra cisla
    if cifra % 2 ==0:  #ak je zvysok po deleni dvoma 0 tak cifra je parna
        pocet += 1 #ak je parna, pocet sa zmeni +1
    n //= 10 #ak nie je parna tak nezvysi pocet, odstrani poslednu cifru a skusa dalsiu
print(pocet)


print("uloha cislo 3")
n=int(input("Zadaj cislo"))
pocet = 0  #pocitadlo cislic
while n > 0:
    pocet += 1 #pri kazdom opakovani +1
    n //= 10 #odstranime poslednu cifru
print(pocet)


print("uloha cislo 4")
n = int(input("Zadaj číslo: "))
vysledok = 0
while n > 0:
    cifra = n % 10 #zoberie poslednu cifru cisla
    vysledok = vysledok * 10 + cifra #posunie vysledok o jedno miesto dolava a prida novu cifru
    n = n // 10 #odstrani poslednu cifru z povodneho cisla
print(vysledok)


print("uloha cislo 7")
#z desiatkovej sustavy do dvojkovej
number=int(input("Zadaj cislo: "))
sucet = 0 #inicializacia cisla 0
moc_des = 0
while number > 0:
    cifra = number % 2
    sucet += cifra * moc_des
    number //= 2
    moc_des= moc_des * 10
print(f"cislo v dvojkovej sustave je {sucet}")


print("uloha cislo 8")
#z dvojkovej sustavy do desiatkovej
number=int(input("Zadaj cislo: "))
sucet = 0
moc_dva = 1
sustava = 10 #desiatkova sustava
while number > 0:
    cifra = number % sustava #da prec poslednu cifru
    sucet += cifra * moc_dva
    number //= sustava
    moc_dva= moc_dva * 2
print(f"cislo v dvojkovej sustave je {sucet}")


print("uloha cislo 9")
n = int(input("Zadaj cislo: "))
povodne = n
opacne = 0 #do tejto premennej sa sklada cislo odzadu
while n > 0:
    cifra = n % 10 #ziskame poslednu cifru cisla
    opacne = opacne * 10 + cifra #prida ziskanu cifru do obrateneho cisla
    n = n // 10 #odstrani poslednu cifru a pokracuje
    if povodne == opacne:
        print("cislo je symetricke")
    else:
        print("cislo nie je symetricke")


print("uloha cislo 10")
# ci je cislo prvocislo
number=int(input("Zadaj cislo: "))
delitele = 0
for i in range (2, int(number**0.5)):
    if number % i == 0:
        delitele *=1
        print("nie je to prvocislo")
if delitele == 0:
    print("prvocislo ako repa!!!!!")


print("uloha cislo 11")
#vypise prvociselny rozklad cisla
number=int(input("Zadaj cislo: "))
delitel=2
while number !=0:
    if number % delitel ==0:
        print(delitel, end=",")
        number = number//delitel #celociselne delenie????
    else:
        delitel +=1


print("uloha cislo 12")
#vypise vsetkych delitelov
number = int(input("Zadaj číslo: "))
delitel = 1 #zaciname 1 lebo kazde cislo je delitelne 1
while delitel <= n: #skusa od 1 az po zadane cislo
    if n % delitel == 0: #ak je zvysok po deleni 0 = je to delitel a vypise ho
        print(delitel)
    delitel = delitel + 1 #vyskusa dalsie cislo


print("uloha cislo 13")
#Collatzova postupnost = ak je cislo parne tak n//2, ak nie tak n*3+1
number = int(input("Zadaj číslo: "))
while number != 1: #cyklus pokracuje kym sa number nerovna 1
    print(number)
    if number % 2 == 0: #skontroluje ci je cislo parne
        number = number // 2 #ak je cislo parne vydeli dvoma
    else:
        number = 3 * number + 1
print(1)