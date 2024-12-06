# continue - break

"""
for number in range(1, 101):
    if number % 2 == 0:
        continue
    # if number == 5:
    #     continue # Avanza a la siguiente iteracion

    print(number)
"""

for number in range(1, 101):
    if number % 2 == 0:
        continue

    if number == 9:
        break # Finalizar un ciclo

    print(number)