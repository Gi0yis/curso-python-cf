# Closures --> Es una función anidada la cual tiene memoria(recuerdan) y pueden acceder a variables que fueron creadas dentro de su entorno

def multiply(number1): # Local

    def operation(number2):
       return number1 * number2
    
    return operation

var1 = 10

func_operation = multiply(var1)

var1 = 20

print(">>> El resultado es:")
result = func_operation(3)
print(result)