class TestExample:
    def test_check_math(self):
        phrase = input("Set a phrase: ")
        assert 0 != len(phrase) <= 15, "whrong text size"
        print('Done!')
