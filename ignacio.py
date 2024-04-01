#Este es el desafío de apis opcional pero no tan opcional parece

#----------------------PREGUNTA 2 ------------------------
# Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el diccionario de respuesta en una variable llamada created_user e imprímala en pantalla.


'''Obtenga toda la información de los usuarios retornada por la API, guárdela en una
variable llamada users_data e imprímala en pantalla.'''

import requests

url = "https://reqres.in/api/users"

#incorporamos la data a entregarle a la API a través del metodo post en el payload
payload={"name": "Ignacio",
    "job": "Profesor"}
headers = {}

created_user = requests.request("POST", url, headers=headers, data=payload)
print(created_user, created_user.text) #devuelve tanto el código como la información del POST


