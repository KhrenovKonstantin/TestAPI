import requests

method = {"method": "POST"}
method1 = {"method": "GET"}
method2 = {"method": "PUT"}
method3 = {"method": "DELETE"}

method_all = (method, method1, method2, method3)

params = method1
data = method
for i in method_all:
    for j in method_all:
        if i == {"method": "GET"}:
            params = i
        else:
            params = i

first_response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
second_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=params)
third_response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
four_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)


print("Запрос POST")
print(first_response.text)
print(second_response.text)
print(third_response.text)
print(four_response.text)
print("-------------")

method.update(method1)

first_response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
second_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
third_response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
four_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)

print("Запрос GET")
print(first_response.text)
print(second_response.text)
print(third_response.text)
print(four_response.text)
print("-------------")

method.update(method2)

first_response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
second_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
third_response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
four_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)

print("Запрос PUT")
print(first_response.text)
print(second_response.text)
print(third_response.text)
print(four_response.text)
print("-------------")

method.update(method3)
first_response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
second_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
third_response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
four_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)

print("Запрос DELETE")
print(first_response.text)
print(second_response.text)
print(third_response.text)
print(four_response.text)
print("-------------")

