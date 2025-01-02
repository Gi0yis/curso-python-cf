# scope (alcance)
# global - local

username = 'Cody' # Global

def show_info():
    # global username # NO RECOMENDADO. Se puede modificar una variable global usando "global". Se recomienda usar una varible global solo para lectura.
    username = 'Codifo Facilito' # Local
    # username = 'Eduardo!!!'
    # last_name = 'facilito'
    # print(id(username))
    print(username)
    # username = 'CodifoFacilito' # NO se puede modificar una variable global de esta manera, dentro de una función
    # username = 'CodifoFacilito'

show_info()
# print(id(username))
print(username)
# print(last_name) # no se puede, es una variable local