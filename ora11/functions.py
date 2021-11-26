import random
import math

print(chr(80), chr(121), chr(116), chr(104), chr(111), chr(110), sep="")
print(ord("P"))
print(ord("a"))
print(ord("A"))
print(ord(chr(80)))
print(float("3.5"))
print(type(float("3.5")))
print(int("12", base = 16)) #számrendszerbeli átírás, 16-osba
print(hex(18))
print(bin(18))
print(oct(18))
number = 23.249352
print(number)
print(round(number))
print(round(number, 2))
print(round(number, 0))

#chr(9999999) különböző hibaüzenetek
print(float("5"))

print("Adja meg a km értéket:")
km_per_hour = int(input())
m_per_sec = km_per_hour * 1000 / 60 / 60
print(m_per_sec)

list = []
for i in range(20):
    list.append(random.randint(0, 100))
print(list)
list_even = []
list_odd = []
i = 0
while i < 20:
    if(list[i] % 2 == 0):
        list_even.append(list[i])
    else:
        list_odd.append(list[i])
    i = i + 1
print(list_even)
print(list_odd)

print("Adja meg a háromszög oldalait:")
a = int(input())
b = int(input())
c = int(input())
if (a + b) > c and (a + c) > b and (b + c) > a:
    d = (a + b + c) / 2
    t = math.sqrt((d * (d - a) * (d - b) * (d - c)))
    k = a + b + c
    print("A háromszög kerülete:", k, "\tA háromszög területe:", t)
else:
    print("A háromszög nem szerkeszthető")

list = []
print("Adja meg a lista elemeit:")
while i != "":
    i = input()
    if i != "":
        list.append(i)
print(list)

list2 = []
for i in range(20):
    list2.append(random.randint(1, 100))
print(list2)

min = list2[0]
max = list2[0]

for i in range(20):
    if min > list2[i]:
        min = list2[i]
    if max < list2[i]:
        max = list2[i]
print("A minimum:", min, "A maximum:", max)

nev = input("Adja meg a nevét: ")
nem = input("Adja meg a nemét: ")
if nem == "férfi":
    print(nev, "Úr")
elif nem == "nő":
    print(nev, "Asszony")
else:
    print(nev)
