
import requests

url = "https://example.com/public/quotes/quote/random"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)