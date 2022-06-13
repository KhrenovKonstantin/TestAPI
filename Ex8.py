import requests
import json
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
method1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

method = json.loads(method1.text)

method_response_text = method1.json()
token_my = method_response_text["token"]
time_me = method_response_text["seconds"]

if token_my in method_response_text ["token"]:
    print(f" {token_my} is correct to this link")

else:
    print("No job linken to this token")

data = {"token": token_my}

response_post = requests.post(url, data)
parsed_response_post = response_post.json()
status_response = parsed_response_post["status"]
print(f"status = '{status_response}', status code = '{response_post.status_code}' . Please wait {time_me} seconds until")

time.sleep(time_me)

response_post = requests.post(url, data)
parsed_response_post = response_post.json()
status_response = parsed_response_post["status"]
result_response = parsed_response_post["result"]
print(f"status = '{status_response}', result = '{response_post}' and status code = '{response_post.status_code}'")
#print(token_my)

#print(time_me)

#method1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",params=method)

#print(method1.json())
#time.sleep(3)
