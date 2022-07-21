import pytest
from cmplex import C
from random import randint
# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku
class Test:
    def test_A(self):
        assert C(0,0) == C(0,0)
        assert C(-1, 1) == C(-1, 1)
        assert C(1, 0) == C(1, 0)
        assert C(0, 1) == C(0, 1)

    def test_B(self):
        for _ in range(100):
            x = randint(10**4, 10**5)
            y = randint(10**6, 10**7)
            assert C(x, y) == C(x, y)