#Este es el desafío de apis opcional pero no tan opcional parece

#----------------------PREGUNTA 4 ------------------------
'''Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla.  '''

import requests

url = "https://reqres.in/api/users/6"

#incorporamos la data a entregarle a la API a través del metodo post en el payload
payload={}
headers = {}

delete_user = requests.request("DELETE", url, headers=headers, data=payload)
print(delete_user, delete_user.text) #devuelve tanto el código como la información del POST
#el codigo 204 es el que esperamos para confirmar delete segun documentacion