consumption_highway = 6 # l
consumption_city = 10 # l
distance_highway = 240 # km
distance_city = 36 # km
half_consumption = consumption_highway * distance_highway / 100 + consumption_city * distance_city / 100
print("Odafelé a fogyasztás:", half_consumption)
full_consumption = 2 * half_consumption
print("Fogyasztás oda-vissza:", full_consumption)
price_of_gas = 460 # Ft
sum_of_gas = full_consumption * price_of_gas
print("Az üzemanyag teljes ára:", sum_of_gas)
sum_of_vacation = 70000
sum_of_money = sum_of_gas + sum_of_vacation
print("El tudunk menni az útra:", sum_of_money < 90000)