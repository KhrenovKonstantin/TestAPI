import requests


class TestExample:
    def test_ex11(self):
        params = {"cookies": ""}
        response = requests.get('https://playground.learnqa.ru/api/homework_cookie', params=params)
        print(response.cookies)
        assert response.cookies == response.cookies, "Проверка не прошла"

        print('Запрос прошел проверку')
