name = 'Giovanni'
last_name = 'García'

# 4 - format
# base = 'El nombre completo es: {} {}. Su edad es: {}'
# full_name = base.format(name, ast_name, 30)

base = 'El nombre completo es: {name} {last_name}. Su edad es: {age}. Activo: {active}'

full_name = base.format(
    age=30, 
    name=name, 
    last_name=last_name, 
    active=True
    )

print(full_name)

# name = input('Ingresa tu nombre: ')
# last_name = input('Ingresa tu apellido: ')
# age = input('Ingrese su edad: ')

# full_name = base.format(name, last_name, age)

# print(full_name)