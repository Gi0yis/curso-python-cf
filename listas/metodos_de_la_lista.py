#             0         1         2       3         4
#            -5        -4        -3      -2        -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)
new_courses = ["React", "Next"]

# Añade un elemento al final de la lista
courses.append("Ruby on Rails")
courses.append("PHP")
courses.append("Laravel")

# Recibe el indice donde queremos incerta el valor y el valor, desplaza a la derecha los valores ya existantes
courses.insert(0, "Rust")
courses.insert(4, "C#")
courses.insert(2, "MySQL")

# Añador una lista a otra
courses.extend(new_courses)

# Saber si un elemento se encuentra en la lista devuelve (True o False)
print(
    "Vue" in courses
)

# Saber si un elemento se encuentra en la lista devuelve su indice
# Si existe un valor devuelve --> ValueError: 'Vue' is not in list
# print(
#     courses.index("Vue")
# )

# Eliminar elementos de una lista
courses.remove("Python")
courses.remove("Django")

# Expulsa el ultimo valor de la lista y retorna su valor 
last_element = courses.pop()
firt_elment = courses.pop(0)

# print(
#    "Python" in courses
# )

# Limpiar nuestra lista (Remueve todos los elementos)
courses.clear()

print(last_element)
print(firt_elment)

print(courses)
print(len(courses))