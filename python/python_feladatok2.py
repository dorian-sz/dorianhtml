#5. feladat
print("Ötödik feladat")
c = int(100000)
t = int(input("Adja meg az évek számát: "))
r = float(0.08)
m = int(12)
FV = c * (1 + r/m)**(m*t)
print("Érték: ", FV)

#6. feladat
print("Hatodik feladat")
print("Ekkor fog csörögni az ébresztő: ", 65 % 24, "órakkor")

#7. feladat
print("Hetedik feladat")
akt_ido = int(input("Adja meg hogy hány óra van: "))
ebreszto = int(input("Adja meg hány óra múlva ébresszen: "))
print((akt_ido + ebreszto) % 24, "órakkor fog ébreszteni.")