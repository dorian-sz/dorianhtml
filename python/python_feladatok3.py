####1. feladat
print("Első feladat")
for i in range(1000):
    print("Szeretjük a Python teknőcöket!")

####3. feladat
print("Harmadik feladat")
honap = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Agusztus", "Szeptember", "Október", "November", "December"]
for index, i in enumerate(honap):
    print("Az év", str(index+1) + ". hónapja " + i)

####4. feladat
import turtle

turtle.left(3645)

####5. feladat
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("5. a")
for i in xs:
    print(i)

print("5. b")
for i in xs:
    print(i*i)

print("5. c")
osszeg = 0
for i in xs:
    osszeg += i 
print(osszeg)

print("5. d")
osszeg = 1
for i in xs:
    osszeg *= i
print(osszeg)

####6. feladat
import turtle
print("Hatodik feladat")
t = turtle.Turtle()
def trtlDraw(length, angle, sides):
    for i in range(sides):
        t.forward(length)
        t.left(angle)
        
trtlDraw(100,120,3)
trtlDraw(100,90,4)
trtlDraw(100,60,6)
trtlDraw(100,45,8)

##7. feladat
print("Hetedik feladat.")
fordulatok = [160, -43, 270, -97, -43, 200, -940, 17, -86]

##8. feladat
print("Nyolcadik feladat")
for i in fordulatok:    
    t.left(i)
    t.forward(100)
print("Kalóz iránya: ", t.heading())

##9. feladat
print("Nyolcadik feladat.")
for i in range(18):    
    t.left(20)
    t.forward(100)

##10. feladat
t = turtle.Turtle()
print(type(t))

