import random

print(random.randint(0, 400))
print(random.random())

a = random.randint(-100, 100)
print(a)
if a > 0:
    print("a szám pozitív")
elif a < 0:
    print("a szám negatív")
else:
    print("a szám nulla")