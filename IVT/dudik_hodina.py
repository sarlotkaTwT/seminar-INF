#hadaj cislo hra
import random #random cislo importovane z kniznice
c=random.randint(1,100)#cislo, kt. hadam
t=0 #tip
while t!=c:
    t=int(input("hadaj cislo "))
    if t>c:
        print("cislo je mensie")
    else:
        print("cislo je vacsie")
print("uhadol si!!!")


#scitavanie parnych cifier
number=int(input("zadaj mi cislo: "))
sucet=0
while number>0:
    cifra = number % 10
    if cifra % 2 ==0: #zvysok po deleni 2
        sucet+= cifra
    number //= 10
print(f"sucet parnych cisel je {sucet}")


#scitavanie neparnych cisiel
number = int(input("zadaj mi cislo: "))
sucet=0
while number>0:
    cifra = number % 10
    if cifra % 2 ==1:
        sucet +=cifra
    number //=10
print(f"sucet neparnych cisel je {sucet}")