#             0         1         2       3         4       De derecha a izquierda
#            -5        -4        -3      -2        -1       De izquierda a derecha
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)

"""
print(
    courses[0]
)

value = courses[4]

# la función en recibe una colección y retorna la cantidad de elementos que la colección almacene.
print(
    len(courses)
)

last_index = len(courses) - 1 # Obtiene el ultimo valor de la lista.

value = courses[len(courses) - 1]

# indices negativos
value = courses[-3]

# Con un valor de indice que no existe: IndexError: list index out of range
value = courses[20]
"""

# Actualizar o remplazar valores
courses[0] = "Ruby on Rails"
courses[1] = "MySQL"

value = courses[0]

print(
    value
)

print(
    courses
)