number = 35
if number > 100:
    print("A szám nagyobb, mint 100.")
else:
    print("A szám nem nagyobb, mint 100.")

if number % 2 == 0:
    print("Páros.")
else:
    print("Páratlan.")

number1 = 3
number2 = 9
if number2 % number1 == 0:
    print(number1, "osztója", number2, "-nek")
else:
    print(number1, "nem osztója", number2, "-nek")

radar ="radar2"
if radar[0] == radar[-1]:
    print("Az első és utolsó betű megegyezik")
else:
    print("Az első és utolsó betű nem egyezik meg.")

a=-1
if a>0:
    print("a szám pozitiv")
elif a<0:
    print("a szám negativ")
else:
    print("a szám nulla")

a = 3
b = 4
c =2

if a >= b and a >=c:
    print("Az a valtozo a legnagyobb")
    if(b>=c):
        print("A c változó a legkisebb")
    else:
        print("A b változó a legkisebb")
else:
    if b>=c:
        print("A b változó a legnagyobb")
        if a>c:
            print("A c valtozo a legkisebb")
        else:
            print("Az a valtozo a legkisebb")
    else:
        print("A c változó a legnagyobb")
        if a>b:
            print("A b valtozo a legkisebb")
        else:
            print("Az a valtozo a legkisebb")

a = 17
if a >= 3 and a < 17:
    print("Beleesik az intervallumba")
else:
    print("Nem esik bele.")

a = 3
b = 4
c = 2

if (a + b > c and b + c > a and c + a > b):
    print("A háromszög szerkeszthető")
else:
    print("A háromszög nem szerkeszthető")

try:
    osztalyzat = int(input())

    if osztalyzat == 1:
        print("elegtelen")
    elif osztalyzat == 2:
        print("elegseges")
    elif osztalyzat == 3:
        print("kozepes")
    elif osztalyzat == 4:
        print("jo")
    elif osztalyzat > 5 or osztalyzat < 1:
        print("nem")
    else:
        print("jeles")
except ValueError:
    print("nem számjegyekből állt a bemenet")

try:
    print(type(float(input("Kérek egy valós számot: "))))
except ValueError:
    print("Hibás bemenet")

print(type(str(7)))
print(type(str(-91.34)))

try:
    szam = input()
    szam = float(szam)
    print(szam*3)
except ValueError:
    print("Nem szám.")