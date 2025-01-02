def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    
    return balance - amount

def handle_operation(callback, *args, **kwargs): # Función de orden superior --> reciben funciones como parametro "Callback".
    print(">>> Comenzando la operación...")
    result = callback(*args, **kwargs) # Callback --> es la función que se recibe como parámetro.
    print('El resultado es', result)

options = {
    'deposit': deposit,
    'withdraw': withdraw
}

option = input('Ingresa una opción (deposit/withdraw): ')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))

function = options.get(
    option,
    lambda *args, **kwargs: 'Lo sentimos, opción NO valida.'
) # Funcion de orden superior

handle_operation(
    function,
    balance,
    amount
)