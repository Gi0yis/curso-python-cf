from random import randint

# Juego número aleatorio

number = None
random_number = randint(0, 10)
hits = 0

while number != random_number and hits < 3:
    number = int(
        input('Ingresa un número:') # str
    )

    if random_number > number:
        print('El número aleatorio es mayor.')
    else:
        print('El número aleatorio es menor.')

    hits += 1

else:
    if number == random_number:
        print(f'>>> Felicidades, encontraste el número {random_number}')
    else:
        print(f'>>> Lo sentimos, no encontraste el número era {random_number}')