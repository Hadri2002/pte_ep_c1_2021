surface = 75 # m^2
surface_per_bucket = 15 # m^2
price_per_bucket = 4300 # Ft
sum_of_paint = 2 * surface / surface_per_bucket * price_per_bucket
print("Összesen", sum_of_paint, "Ft-ba fog kerülni.")
minutes_per_square_meter = 13
hours_per_sqaure_meter = minutes_per_square_meter / 60
hourly_wage = 21000
sum_of_wage = 2 * surface * hours_per_sqaure_meter * hourly_wage
print("ÁFA nélkül:", sum_of_wage)
sum_of_wage *= 1.27
print("ÁFÁval:", sum_of_wage)
