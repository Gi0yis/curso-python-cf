#             0         1         2       3         4
#            -5        -4        -3      -2        -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)

# Con Slicing no modificamos la lista. Pero con estos metodos di se modifica.
# copy
copy_list = courses.copy()
print(copy_list)
# reverse
courses.reverse()
print(courses)
# sort
# Ordena de forma acendente de manera predeterminada
# courses.sort()
# Forma descendente
courses.sort(reverse=True)

print(courses)