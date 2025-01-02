def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    
    return balance - amount

def default(*args, **kwargs):
    return '>>>> Lo sentimos, opción NO valida'

# print(deposit(100, 10))
# print(withdraw(200, 40))

# func1 = deposit
# func2 = withdraw

# print(type(func1))
# print(type(func2))

# print(func1(100, 20))
# print(func2(100, 101))

options = {
    'deposit': deposit,
    'withdraw': withdraw
}

# print(options)

option = input('Ingresa una opción (deposit/withdraw): ')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))

function = options.get(option, default)
total = function(balance, amount)

print(total)
#print(function)