"""
Si una función tiene la capasidad de retornar otras funciones, tambien se le conoce como "Función de orden superior".
"""

def factory_operation(option):
    def deposit(balance, amount=0):
        return balance + amount

    def withdraw(balance, amount=0):
        if amount > balance:
            return None
        
        return balance - amount
    
    default = lambda *args, **kwargs: '>>> Lo sentimos, opción NO valido.'

    if option == 'deposit':
        return deposit
    elif option == 'withdraw':
        return withdraw
    else:
        return default

option = input('Ingresa una opción (deposit/withdraw): ')
func = factory_operation(option)

print(func(100, 20))
print(type(func))