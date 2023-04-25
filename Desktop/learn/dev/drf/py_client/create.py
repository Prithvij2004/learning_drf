import requests

# endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/products/"


data = {
    "title": "Need to fill",
    "price": 32.99
}

get_repsonse = requests.post(endpoint, json=data)
print(get_repsonse.json())
# print(get_repsonse.text)
# print(get_repsonse.status_code)