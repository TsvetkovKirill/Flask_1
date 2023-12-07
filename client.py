import requests

response = requests.post("http://127.0.0.1:5000/advertisements",
                        json={'title': 'Moped', 'description': 'Random notice',
                              'owner': 'kirill'},
                        )

print(response.status_code)
print(response.text)

response = requests.get(
    "http://127.0.0.1:5000/advertisements/1",
)
print(response.status_code)
print(response.text)

response = requests.delete(
    "http://127.0.0.1:5000/advertisements/1",
)
print(response.status_code)
print(response.text)

