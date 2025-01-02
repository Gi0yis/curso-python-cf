"""
def <nombre_de_la_funcion>(<parámetros, >):
    ...
"""

def multiply(number1, number2):

    # print("Hola mundo") # Si se muestra

    return number1 * number2

    print("Hola mundo") # El código despues de return NO se muestra

def full_name(first_name, last_name, prefix):
    return f"{prefix} {first_name} {last_name}"

# result = multiply(10, 20)
# print(result - 10)

# user_full_name = full_name("Giovanni", "López", "Ing.")
# print(f"Hola, el nombre del usuario es: {user_full_name}")

def division(number1, number2):
    if number1 == 0 or  number2 == 0:
        return None # Corto circuito
    
    return number1 / number2

print(
    division(10, 0)
)