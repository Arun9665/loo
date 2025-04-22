
import requests

def api_hendling():

    url = "https://freeapi.miniprojectideas.com/api/amazon/GetAllSaleByCustomerId"

    headers = {"accept": "application/json"}

    responce = requests.get(url, headers=headers)
    print(responce.text)

api_hendling()
