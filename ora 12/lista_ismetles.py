def rendezes(lista: list[int]) -> list[int]:
    rendezett_lista = lista.copy()
    for i in range(1, len(lista)):
        for j in range(len(lista) - i):
            if rendezett_lista[j] > rendezett_lista[j + 1]:
                seged = rendezett_lista[j]
                rendezett_lista[j] = rendezett_lista[j + 1]
                rendezett_lista[j + 1] = seged

    return rendezett_lista

def minimum(lista: list[int], hanyadik = 2) -> int:
    return rendezes(lista)[hanyadik]

def osszeg(lista: list[int]) -> int:
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg

def atlag(lista: list[int]) -> float:
    return osszeg(lista) / len(lista)

print(rendezes([56, 43, 24, 79, 31, 1243, 65, 32, 56]))
print(minimum([23, 56, 31, 21, 46, 89, 2, 45, 78]))
print(osszeg([3, 4, 5]))
print(atlag([3, 4, 5]))

