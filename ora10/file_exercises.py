"""
Írjon programot, ami soronként beolvassa a lorem.txt fájl tartalmát
 és megjeleníti a kijelzőn!
"""
fileobject = open("lorem.txt", "r")
sor = fileobject.readline()
while len(sor)>0:
    # print(sor)
    sor = fileobject.readline()
fileobject.close()
"""
Írjon programot, ami beolvassa a lorem.txt fájl tartalmát és kiírja a konzolra,
 a leghosszabb sorát!
"""
fileobject=open("lorem.txt","r")
leghosszabb=fileobject.readline()
for sor in fileobject:
    if len(leghosszabb)<len(sor):
        leghosszabb=sor
print(leghosszabb)
fileobject.close()

"""
Írjon programot, ami átmásolja egyik fájl tartalmát egy másikba!
"""

fileobject = open("lorem.txt", "r")
fileobject2 = open("lorem_copy.txt", "w")
fileobject2.write(fileobject.read())
fileobject.close()
fileobject2.close()


"""
Az előző programot módosítsa úgy, hogy minden szóközt 3 másikra cseréli!
"""

fileobject = open("lorem.txt", "r")
fileobject2 = open("lorem_copy.txt", "w")
szoveg = fileobject.read()
for karakter in szoveg:
    if karakter == " ":
        fileobject2.write("   ")
    else:
        fileobject2.write(karakter)
fileobject.close()
fileobject2.close()


"""
Írjon programot, ami 2 fájlt tartalmát egy harmadikba fésüli össze!
"""

fileobject1 = open("fajl1.txt", "r")
fileobject2 = open("fajl2.txt", "r")
fileobject3 = open("fajl3.txt", "w+")

sor1 = fileobject1.readline()
sor2 = fileobject2.readline()

while len(sor1) > 0 or len(sor2) > 0:
    fileobject3.write(sor1)
    fileobject3.write(sor2)
    sor1 = fileobject1.readline()
    sor2 = fileobject2.readline()

fileobject1.close()
fileobject2.close()
fileobject3.close()