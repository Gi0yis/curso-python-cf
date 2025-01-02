"""
Decoradores --> Es una función que nos permite añadir nuevas funcionalidades a otras funciones.
Para poder añadir nuevas funcionalidades no es necesario modificar las funciones base.
"""

# A(B) -> C
# A (Decorador)
# B (Función a decorar (Base))
# C (Función decorada Base + Nuevas líneas de código)

            # B
def decorator(func): # A

    def wrapper(*args, **kwargs): # C
        print(">>> Antes del llamado")
        # func() 
        result = func(*args, **kwargs)
        print(">>> Después del llamado")
        
        return result
    
    return wrapper

@decorator
def hello_world():
    print("Hola Mundo")

@decorator
def suma(number1, number2):
    return number1 + number2

print(suma(10, 20))