def outer_function():
    message = 'Hola, nos encontramos en una función anidada.'

    def inner_function():
        # info = 'Info value'
        # message = 'Info value' # crea una nueva variable
        nonlocal message # Indicar que es una varible no local, se encuentra en un bloque superior
        message = 'Info value'

        # print(message)
    inner_function()
    print(message)
    

outer_function()