"""
def <nombre_de_la_funcion>(<parámetros, >):
    ...
"""

def foo():
    return "Cody", True, 12 # Tupla

# result = foo()
# print(result)
# print(type(result))

# username, active, age = foo()
username, _, age = foo()

print(username, age)