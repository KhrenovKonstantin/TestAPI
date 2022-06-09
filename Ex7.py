import requests

method = {"method": "POST"}
method1 = {"method": "GET"}
method2 = {"method": "PUT"}
method3 = {"method": "DELETE"}
first_response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
second_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
third_response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
four_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)


print("Запрос POST")
print(first_response.text)
print(second_response.text)
print(third_response.text)
print(four_response.text)
print("-------------")

if method != {"method": "GET"}:
    method = method1
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

if method != {"method": "PUT"}:
    method = method2
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

if method != {"method": "delete"}:
    method = method3
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

