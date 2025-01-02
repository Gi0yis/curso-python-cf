# Las listas son mutables / Las tuplas son inmutables
#               0          1     2
#              -3         -2    -1
settings = ("localhost", 3306, True)

print(settings)
print(type(settings))

print("---------------")
# settings[0] = "127.0.0.1" --> No se puede modificar una tupla

print(settings[0])
print(settings[1])
print(settings[2])

print(settings[-1])

print("---------------")

# print(settings[10]) --> Error (Indice no existe)

# tupla sin parentecis
#numbers = 1, 2, 3, 4, 5
# Tupla de un solo elemento
numbers = 1,

print(numbers)
print(type(numbers))