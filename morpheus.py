#Este es el desafío de apis opcional pero no tan opcional parece

#----------------------PREGUNTA 3 ------------------------
'''Actualice un usuario llamado morpheus para que tenga un campo llamado residence igual a zion. Guarde el diccionario de respuesta en una variable llamada
updated_user e imprímala en pantalla. '''

import requests

url = "https://reqres.in/api/users/1"

#incorporamos la data a entregarle a la API a través del metodo post en el payload
payload={"name": "morpheus",
    "residence": "zion"}
headers = {}

updated_user = requests.request("PUT", url, headers=headers, data=payload)
print(updated_user, updated_user.text) #devuelve tanto el código como la información del POST

