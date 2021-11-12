mass = 40 # kg
syrup_per_kg = 0.6 # l
dl_per_bottle = 7.5 # dl
full_bottles = mass * syrup_per_kg * 10 // dl_per_bottle
print(full_bottles)