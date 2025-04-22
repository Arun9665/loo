
import requests

add_url = "https://freeapi.miniprojectideas.com/api/amazon/GetAllSaleByCustomerId"

respons = requests.get(add_url)

print(respons.text)