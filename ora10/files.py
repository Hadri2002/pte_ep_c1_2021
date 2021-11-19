try:
    fileobject = open("lorem.txt", "r")
    tartalom = fileobject.read(10)
    tartalom = fileobject.read(10)
    tartalom = fileobject.read(10)
    print(tartalom)
    """tartalom = fileobject.readline()"""
    tartalom = fileobject.readlines()
    print(tartalom)
    print(type(tartalom))
    print(len(tartalom))
    print(fileobject.tell())
    fileobject.close()
except FileNotFoundError:
    print("Nem található ilyen fájl.")

fileobject2 = open("lorem5.txt", "w")
fileobject2.write("Python")
fileobject2.flush()
fileobject2.write("Python")
fileobject2.close()
