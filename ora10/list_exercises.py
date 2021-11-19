"""
Írjon programot, ami összefésüli a month és days_in_month listákat úgy,
hogy minden hónap nevét a hónapban lévő napok száma kövessen az új listában:
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  month = [’január’, ’február’, ’március’, ’április’, ’május’,
   ’június’, ’július’, ’augusztus’, ’szeptember’, ’október’, ’november’, ’december’]
"""
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ['január', 'február', 'március', 'április', 'május', 'június',
'július', 'augusztus', 'szeptember', 'október', 'november', 'december']


months_and_days = []
for i in range(12):
    months_and_days.append(month[i])
    months_and_days.append(days_in_month[i])
print(months_and_days)

"""
Írjon programot, ami megkeresi egy számokat tartalmazó lista legnagyobb elemét!
"""
szamok = [34, 97, 12, -15, 35, 10]

max=szamok[0]

for i in range(len(szamok)):
    if(szamok[i]>max):
        max=szamok[i]

print(max)

min = szamok[0]
hely=0
for i in range(len(szamok)):
    if(szamok[i] < min):
        min = szamok[i]
        hely=i
"""for i in range(len(szamok)):
    if(szamok[i] == min):
        print(i)
        """
print(hely)