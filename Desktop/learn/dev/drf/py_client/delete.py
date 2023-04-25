import requests

product_id = input("What is the product id you want to use?\n")

try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not a valid id')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_repsonse = requests.delete(endpoint)
    print(get_repsonse.status_code, get_repsonse.status_code==204)
