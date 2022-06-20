import pytest
import requests


class TestFirstAPI:
    users = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, '
         'like Gecko) Version/4.0 Mobile Safari/534.30'),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 '
         'Mobile/15E148 Safari/604.1'),
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
         'Safari/537.36 Edg/91.0.100.0'),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
         'Version/13.0.3 Mobile/15E148 Safari/604.1')
    ]

    @pytest.mark.parametrize('user_agent', users)
    def ex13(self, user_agent):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        data = {'user_agent': user_agent}

        response = requests.get(url, headers=data)

        assert response.status_code == 200, 'Wrong code'

        response_dict = response.json()
        assert "platform" in response_dict, 'platform not found'
        assert "browser" in response_dict, 'browser not found'
        assert "device" in response_dict, 'device not found'

        print(response.text)
