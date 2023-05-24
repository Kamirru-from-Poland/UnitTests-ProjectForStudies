import unittest

def oblicz_pierwiastki(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1, x2

class TestObliczPierwiastki(unittest.TestCase):
    def test_brak_pierwiastkow(self):
        # Sprawdzamy, czy dla a=0, równanie nie ma pierwiastków
        postac_ogolna = (0, 2, 3)
        self.assertRaises(ZeroDivisionError, oblicz_pierwiastki, *postac_ogolna)

    def test_jeden_pierwiastek(self):
        # Sprawdzamy, czy dla równania z jednym pierwiastkiem otrzymamy poprawny wynik
        postac_ogolna = (1, -4, 4)
        expected_result = 2
        self.assertEqual(oblicz_pierwiastki(*postac_ogolna), expected_result)

    def test_dwa_pierwiastki(self):
        # Sprawdzamy, czy dla równania z dwoma pierwiastkami otrzymamy poprawne wyniki
        postac_ogolna = (2,-7,3)
        expected_result = (3, 0.5)
        self.assertEqual(oblicz_pierwiastki(*postac_ogolna), expected_result)

    def test_delta_ujemna(self):
        # Sprawdzamy, czy dla ujemnej delty funkcja zwraca None
        postac_ogolna = (1, 2, 3)
        self.assertIsNone(oblicz_pierwiastki(*postac_ogolna))

if __name__ == '__main__':
    # postac_ogolna = (1,6,8)
    # print(oblicz_pierwiastki(*postac_ogolna))
    unittest.main()