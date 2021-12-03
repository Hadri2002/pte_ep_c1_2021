def menu_opciok():
    print("Válasszon az alábbi menüpontok közül:\n\t0 - Kilépés"
          "\n\t1 - Új fa rögzítése"
          "\n\t2 - Fajta lekérdezése")

def egesz_szam_bekerese(koordinata: str) -> int:
    szam = ""
    while szam == "":
        try:
            szam = int(input(f"Adja meg {koordinata} koordinátát: "))
        except ValueError:
            print("Nem egész számott adott meg!")
    return szam

def fa_regisztralasa(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print("Itt már áll egy fa.")
    else:
        fak[hely] = input("Kérem adja meg a fa fajtáját: ")
        print("Sikeres regisztráció!")

def szotar_kiiratasa(szotar, filepath):
    fileobject = open(filepath, "w")
    for kulcs in szotar:
        fileobject.write(str(kulcs[0]))
        fileobject.write("\t")
        fileobject.write(str(kulcs[1]))
        fileobject.write("\t")
        fileobject.write(szotar[kulcs])
        fileobject.write("\n")
    fileobject.close()

def szotar_betoltes(filepath: str):
    szotar = {}
    file = open(filepath, "r")
    for sor in file:
        adat = sor.strip().split("\t")
        szotar[(int(adat[0]), int(adat[1]))] = adat[2]

    file.close()
    return szotar

def fafajta_lekerdezese(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print(fak[hely])
    else:
        print("Ezen a koordinátán nincs fa.")

menu = ""
fak_szotar_filepath = "fak.csv"
fak = szotar_betoltes(fak_szotar_filepath)
while menu != "0":
    menu_opciok()
    menu = input()
    if menu == "1":
        fa_regisztralasa(fak)
    elif menu == "2":
        fafajta_lekerdezese(fak)
szotar_kiiratasa(fak, fak_szotar_filepath)