print("Uloha cislo 4")
n=int(input("Zadaj cislo:"))
for n in range(1,n+1):
    print(n,n**2)



print("Uloha cislo 5")
x=int(input("Zadaj cislo odkial:"))
y=int(input("Zadaj cislo pokial:"))
for z in range(x,y+1):
    odmocnina= round(z**0.5,2)
    print(z, odmocnina)



print("Uloha cislo 6")
for x in range(1,21):
    if x==3:
        print(f"x={x},Funkcia nie je definovana")
    else:
        y= (x**2 - 1)/(x-3)
        print(f"x={x}, y={y}")



print("Uloha cislo 7")
i=int(input("Zadaj cislo:"))
for j in range(1, i+1):
    if j%3==0:
        print(j)



print("Uloha cislo 8")
for a in range(1,21):
    if a%2==0:
        print(a)



print("Uloha cislo 9")
z=int(input("Zadaj cislo - zaciatok:"))
k=int(input("Zadaj cislo - koniec:"))
for l in range(z,k+1):
    if l%2!=0:
        print(l)



print("Uloha cislo 10")
b=int(input("Zadaj cislo:"))
for d in range(b,0,-1):
    print(d)
