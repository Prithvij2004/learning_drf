import requests

# endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/products/"


get_repsonse = requests.get(endpoint)
print(get_repsonse.json())
# print(get_repsonse.text)
# print(get_repsonse.status_code)