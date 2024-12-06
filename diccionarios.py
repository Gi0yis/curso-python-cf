# Clave (llave) : Valor
# String, tuplas, int, float, booleans, funciones --> Objetos inmutables
# Los diccionarios son mutables
# Las llaves son unicas
# Metodos --> keys, values, items
""" user = {
    10: 'Eduardo',
    3.1416: 'Giovanni',
    True: False,
    (1, 2, 3): 'Tupla'
}
"""
user = {
    'name': 'Giovanni',
    'age': 10,
    'activate': True,
    'courses': [
        'Python', 'Django', 'Redis'
    ],
    'settings': (123, True),
}

"""
print('name' in user)

user_name = user['name']
print(
    user_name
)

print(user[3.14])

#                                 Valor por defecto --> None
user_name = user.get('password', 'Lo siento, el valor no existe') # user['password] --> Usar get para evitar errores
print(user_name)

user['last_name'] = 'facilito' # Anadir
user['name'] = 'código' # Actualizar


print(
    user.keys() # Listado de todas las llaves del diccionario
)

print(
    list(user.keys()) # generar una lista de llaves
)

print(
    tuple(user.keys()) # generar una tupla de llaves
)

print(
    user.values()
)

print(
    list(user.values())
)


print(
    user.items() # Lista de tuplas
)

print(
    list(user.items())
)

"""

# Actualizar diccionarios en tiempo de ejecución

# user['name'] = 'Código' # Actualizar
# user['last_name'] = 'Facilito' # Añadir llave

"""
Añadir o actualizar valores a un diccionarios
user.update({
    'name': 'Código',
    'settings': None,
    'last_name': 'Facilito'
})
"""

user.setdefault('id', 100) # intenta traer el valor de la llave y si no existe lo crea (Parecido a get, pero get no crea llaves)

courses = user.get('courses', []) # añadir valor a una lista
courses.append('Ruby on Rails')
courses.append('Rust')

user.update({
    'name': 'Código',
    'settings': None,
    'last_name': 'Facilito',
    'courses': courses
})

# Eliminar una llave y su valor
del user['courses']
value = user.pop('settings') # Extrae y luego elimina el valor

user.clear() # Limpiar el diccionario

print(len(user))
print(user)