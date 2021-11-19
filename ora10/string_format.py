number = 5
number2 = 2 * number
print("A number valtozo erteke:", number, "\b. Ha megszorzom kettővel, akkor:", number2, "\b-t kapok.")
print("A number valtozo erteke: ", number, ". Ha megszorzom kettővel, akkor: ", number2, "-t kapok.", sep = "")
print(f"A number valtozo erteke: {number}. Ha megszorzom kettővel, akkor: {number2}-t kapok.")
print("A number valtozo erteke: {}. Ha megszorzom kettővel, akkor: {}-t kapok.".format(number,number2))

# Igazítások
print(f"A number valtozo erteke: {number:<3}. Ha megszorzom kettővel, akkor: {number2:>3}-t kapok.")
print("A number valtozo erteke: {:^3}. Ha megszorzom kettővel, akkor: {:^4}-t kapok.".format(number,number2))

# Számformátumok
print(f"A number valtozo binaris erteke: {number:b}")
print("A number valtozo oktalis erteke: {:o}".format(number))
print(f"A number valtozo decimalis erteke: {number:d}")
print("A number valtozo hexadecimalis erteke: {:x} es {:X}".format(number, number))

# Unicode karakter
number = 65
print(f"{number:c}")

# Valós számok
number = 100.1232
print(f"Tudományos: {number:e} vagy {number:E}")
print(f"Valós szám: {number:f}")
print(f"3 tizedesjegy pontosság: {number:.3f}")
print(f"15 karakteren {number:15f}")
print(f"15 karakteren 3 tizedesjegy pontosság: {number:15.3f}")
print(f"Százalékos érték: {number:%}")
print(f"3 tizedesjegy pontosság: {number:.3%}")
print(f"15 karakteren: {number:15%}")
print(f"15 karakteren, 3 tizedesjegy pontosság: {number:15.3%}")
