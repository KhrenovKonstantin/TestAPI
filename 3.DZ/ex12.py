import requests


class TestExample:
    def test_ex12(self):
        params = {"headers": ""}
        response = requests.get('https://playground.learnqa.ru/api/homework_header', params=params)
        print(response.headers)
        assert response.status_code == 200, "Проверка не прошла"
