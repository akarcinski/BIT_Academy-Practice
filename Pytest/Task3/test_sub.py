import pytest
from cmplex import C
from random import randint
# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku
class Test:
    def test_A(self):
        assert C(0, 0) - C(0, 0) == C(0, 0)
        assert C(2, 2) - C(2, 2) == C(0, 0)
        assert C(3, 0) - C(3, 0) == C(0, 0)
        assert C(0, 3) - C(0, 3) == C(0, 0)
    
    def task_B(self):
        for _ in range(100):
            x = randint(10**4, 10**5)
            y = randint(10**6, 10**7)
            z = randint(10**2, 10**3)
            w = randint(0, 100)
            assert C(x, y) - C(z, w) == C( x - z , y - w )