import requests
import json

respounse = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_respounse = respounse.history[0]

print(respounse.history)
print(first_respounse.url)
print(respounse.url)