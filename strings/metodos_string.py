title = '  Curso profesional de Python!  '
title= title.strip() # Eliminar espacios al pricipio o al final de

print(title.upper())
print(title.lower())

print(title.find('p')) # Conocer donde de encuenta la primera coincidencia
print('6'.isnumeric()) # devuelve si un string reprecenta un numero

messaje = 'código facilito'
print(messaje.capitalize())

# print(messaje[0].upper() + messaje[1:])
print(f'{messaje[0].upper()}{messaje[1:]}')