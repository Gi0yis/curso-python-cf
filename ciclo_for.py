# for-each:
# Nos permite iterear sobre cada uno de los elementos de una colección donde en cada iteracion obtendremos el valor de cada uno de los elementos.
# numbers = [20, 5, 10, 15, 25]
# numbers = (20, 5, 10, 15, 25)

"""
for <variable> in <collection>:
    ...
"""
# for number in numbers:
#     print("El valor de la variable es:", number)

message = "Hola Mundo"
user = {
    'name': 'Giovanni',
    'age': 31,
    'password': '12345'
}

# for caracter in message:
#     print(caracter)
# print(user.items())

for key, value in user.items():
    print("La llave es", key, "el valor es", value)

# for item in user.items():
#     key, value = item
#     print(key, value)

numbers = [1, 2, 3]

# Ciclo infinito
# for number in numbers:
#     numbers.append(10) --> no recomendado