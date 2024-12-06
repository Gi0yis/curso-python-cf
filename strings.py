# Los strings son inmubles, los usaremos para fines de lectura
# Son colecciones de caracteres a cada caracter le correspode un indice
message = 'Hola mundo!'

print(message)
print(type(message))
print(len(message))

print('!' in message)
print(message.index('!'))
print(message[-1])

# message2 = message[1:]
message2 = 'h' + message[1:]

print(message2)

# message[0] = "h" --> No se pueden modificar
# En lugar de modificar creamos uno nuevo