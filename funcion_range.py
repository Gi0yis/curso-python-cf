# Función Range
# range(10): # 0 -9
# range(start, stop + 1):

# for number in range(5, 10 + 1): # Usar solo si necesito trabajar con rangos 
#     print(number)

courses = ['Python', 'Go', 'Rust', 'Django', 'Java']

# for index in range(len(courses)): # No recomendable
#     print(courses[index])

for course in courses: # recomendado
    print(course)