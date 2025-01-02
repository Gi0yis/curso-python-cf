# * (Posición) - (Tupla)
# ** (Nombres)

def suma(*numbers):
    return sum(numbers)

print(
    suma(10, 20, 4, 5, 7, 10, 7, 8, 9)
)

def show_info(username, email, *scores):
    print(username)
    print(email)

    average = sum(scores) / len(scores)
    print(average)

show_info(
    'Cody',
    'cody@codigofacilito.com',
    10, 10, 8, 9 # Tupla
)

