"""
def <nombre_de_la_funcion>(<parámetros, >):
    ...
"""

def full_name(first_name, last_name, prefix):
    return f'{prefix} {first_name} {last_name}'

print(
    full_name(
        prefix='Mr.',
        first_name='Cody',
        last_name='Facilito'
    )
)

print(
    full_name(
        'Cody',
        'Facilito',
        'Mr.'
    )
)

print(
    full_name(
        'Cody',
        last_name='Facilito',
        prefix='Mr.'
    )
)