import requests

# endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/products/1/update/"

data = {
    "title": "Hello my dear friend",
    "price": 130.00,
}


get_repsonse = requests.put(endpoint, json=data)
print(get_repsonse.json())
# print(get_repsonse.text)
# print(get_repsonse.status_code)