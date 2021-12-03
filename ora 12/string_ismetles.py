def megtalal(szoveg: str, karakter: str) -> int:
    """
    A karakter pozíciójának megkeresése.

    :param szoveg: A szöveg, amiben keressük a karaktert
    :param karakter: Egyetlen karakter, amit keresünk
    :return: A karakter első előfordulása a szövegben, vagy -1 ha nincs benne
    """
    i = 0
    while i < len(szoveg):
        if szoveg[i] == karakter:
            break
        else:
            i = i + 1

    if i == len(szoveg):
        i = -1

    return i

def kacsak(prefixes = "JKLMNOPQ", suffix = "ack") -> None:
    """

    :param prefixes:
    :param suffix:
    :return:
    """
    for elem in prefixes:
        print(elem + suffix)



print(megtalal("alma", "m"))
kacsak()