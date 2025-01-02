#             0         1         2       3         4
#            -5        -4        -3      -2        -1
# [Slicing [start:end]
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)

"""
new_list = [
    courses[0],
    courses[1],
    courses[2]
]

print(
    new_list
)

# Lista de dos indices 0, 1 el indice 2 (end) no es tomado en cuenta.
new_list = courses[0:2]

# Si vamos a iniciar en el indice 0, podemos omitir el valor.
new_list = courses[:3]

# ultimos 3 elemtos
new_list = courses[2:5]

# si queremos el ultimo elemento podemos omitir el valor
new_list = courses[2:]

# Copiar lista completa
new_list = courses[:] # Shallow copy

# Tercer elmentos omitir de n numeros (en este caso omite el valor cada dos elementos)
new_list = courses[::2]
"""

# Invierte el orden
new_list = courses[::-1]

print(new_list)