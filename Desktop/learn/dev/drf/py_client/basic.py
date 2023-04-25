import requests

# endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/"

get_repsonse = requests.post(endpoint,
                            json={"title": "Hello World"})
# print(get_repsonse.json())
print(get_repsonse.text)
# print(get_repsonse.status_code)