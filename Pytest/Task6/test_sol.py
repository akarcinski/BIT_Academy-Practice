import pytest
from random import randint
from solution import Prime_number

class Test_small:
    @pytest.mark.parametrize("test_input,expected", [(0, False), (1, False), (2, True), (3, True), (-5, False)])
    def test_A(self, test_input,expected):
        assert Prime_number(test_input) == expected
    
class Test_medium:
    def test_A(self):
        A = [3001, 1613, 3769, 2551, 5743, 8713, 7043, 6827, 7351, 2711]
        for x in A:
            assert Prime_number(x) == True

    def test_B(self):
        A = [9420, 6493, 1445, 2093, 7519]
        for x in A:
            assert Prime_number(x) == False

    def test_C(self):
        for _ in range(10):
            number = randint(10 ** 4, 10 ** 5)
            result = True
            i = 2

            while i * i <= number:
                if number % i == 0:
                    result = False
                    break
                i += 1
            assert Prime_number(number) == result
@pytest.mark.dependency(depends=["Test_medium::test_A", "Test_medium::test_B", "Test_medium::test_C"])
class Test_big:
    def test_A(self):
        A = [556370881039, 805469181901, 735493327391]
        for x in A:
            assert Prime_number(x) == True
    def test_B(self):
        A = [235389759301, 261333307679, 663012434137, 877538745143, 205409137831, 222222222222]
        for x in A:
            assert Prime_number(x) == False
    def test_C(self):
        for _ in range(10):
            number = randint(10 ** 4, 10 ** 5)
            result = True
            i = 2

            while i * i <= number:
                if number % i == 0:
                    result = False
                    break
                i += 1
            assert Prime_number(number) == result

            
#Don't do that
'''
@pytest.mark.xfail
class Test_destroyer:
    def test_murderer_A(self):
        assert Prime_number(265252859812191058636308479999999) == True
    def test_murderer_B(slef):
        assert Prime_number(35742549198872617291353508656626642567) == True
    def test_killer(self):
        assert Prime_number(6957596529882152968992225251835887181478451547013) == True
    def test_rip(self):
        assert Prime_number(85053461164796801949539541639542805770666392330682673302530819774105141531698707146930307290253537320447270457) == True
'''