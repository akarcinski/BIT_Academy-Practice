from function import square
import pytest
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100 
class test:
    def test_A(self):
        assert square(0) == 0
    def test_B(self):
        assert square(1) == 1
    def test_C(self):
        assert square(-1) == 1
    def test_D(self):
        assert square(100) == 10000