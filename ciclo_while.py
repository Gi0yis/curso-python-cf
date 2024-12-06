# While --> lo vamos a utilizar si no dabemos cuantas veces vamos a iterar

"""
while <condition>:
    ...
"""

"""
counter = 0
while counter < 10:
    print('Valor:', counter)
    # counter = counter + 1
    counter += 1

for number in range(0, 10): # mejor usar for
    print(number)
"""

number = int(
    input('Ingresa un número: ')
)
counter = 0

while number > 0:
    number = number // 10
    counter += 1
else:
    print("La cantidad de digitos es:", counter)