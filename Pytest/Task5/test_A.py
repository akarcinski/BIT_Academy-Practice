import pytest
import random

from function import count_chars

class Test_small:
    @pytest.mark.parametrize("test_input,expected", [("abc", [1,1,1]), ("", [0,0,0]), ("abccababc", [3,3,3]), 
    pytest.param("abcd", [1,1,1], marks=pytest.mark.xfail)])
    def test_A(self, test_input, expected):
        assert count_chars(test_input) == expected
        
class Test_big:
    def test_A(self):
        letters = ['a','b','c']
        for _ in range(10):
            strr = ''.join(random.choice(letters) for i in range(10000))
            assert count_chars(strr) == [strr.count('a'), strr.count('b'), strr.count('c')]

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'