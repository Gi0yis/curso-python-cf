"""
funciones lambda --> funciones sin nombre

sintaxis:
lambda <parámetros>: <body> # Siempre retornan un valor.


# add = lambda number1, number2=0: number1 + number2 # NO es necesario usar return
add = lambda *args: sum(args)

print(add(10, 20, 30, 40, 50, 60, 70))
#print(add(number1=10, number2=20))
"""

def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    
    return balance - amount

options = {
    'deposit': deposit,
    'withdraw': withdraw
}

option = input('Ingresa una opción (deposit/withdraw): ')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))

# default = lambda *args, **kwargs: 'Lo sentimos, opción NO valida.'
# function = options.get(option,default)
function = options.get(option, lambda *args, **kwargs: 'Lo sentimos, opción NO valida.')
total = function(balance, amount)
print(total)