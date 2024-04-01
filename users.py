#Este es el desafío de apis opcional pero no tan opcional parece

#----------------------PREGUNTA 1 ------------------------
#Obtenga toda la información de los usuarios retornada por la API, guárdela en una variable llamada users_data e imprímala en pantalla


import requests

url = "https://reqres.in/api/users"

payload={}
headers = {}

users_data = requests.request("GET", url, headers=headers, data=payload)

print(users_data)
print(users_data.text)

