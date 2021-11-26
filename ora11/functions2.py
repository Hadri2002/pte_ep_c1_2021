import datetime
import random

def maximum_kereses(lista: list[float]) -> float:
    """
    Megkeresi egy valós számokat tartalmazó listának a legnagyobb elemét.
    :param lista: Valós számok listája
    :return: Valós számok maximum értéke
    """
    max = lista[0]
    for number in lista:
        if max < number:
            max = number
    return max

def kiiratas(szam: float) -> None:
    print(szam)

def nevBekeres() -> str:
    nev = input("Adja meg a nevét: ")
    return nev

def koszones(nev: str) -> None:
    print("Üdv " + nev + "!")

def brutto(netto: float) -> None:
    brutto = netto / 0.73
    print(brutto)
    print("Az ÁFA kulcs értéke: 27%")

def get_afa(termek_ara: int, afa=27) -> float:
    """

    :param termek_ara: termék ára forintban
    :param afa: Áfa kulcs %ban
    :return: . . .
    """
    return termek_ara * afa / 100

def brutto(termek_ara: int, afa = 27) -> float:
    return termek_ara + get_afa(termek_ara, afa)

numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))
print(numbers)

maximum = maximum_kereses(numbers)
print(maximum)
kiiratas(maximum)
print(kiiratas(maximum))

nev = ""
nev = nevBekeres()
koszones(nev)
brutto(500)
ar = 10000
print(get_afa(ar))
print(brutto(ar))

