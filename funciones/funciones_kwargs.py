# * (Posición) - (Tupla)
# ** (Nombres) - (Dictionary)


def show_info(**user):
    # print(user) # Imprime un diccionario
    for key, value in user.items():
        print(key, '-', value)

show_info(
    usermane='Cody',
    email='cody@codigofacilito.com',
    password='1234',
    is_active=True,
    courses=('Python', 'Django', 'Flask'),
    last_login='2024',
    is_super_user=True
)