import unittest

from _260224_Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_sucet(self):
        calculator = Calculator()
        vysledok = calculator.sucet(2, 3)
        self.assertEqual(vysledok, 5)

    def test_delenie(self):
        calculator = Calculator()
        vysledok = calculator.delenie(10, 5)
        self.assertEqual(vysledok, 2)

    def test_delenie_nulou(self):
        calculator = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calculator.delenie(6, 0)

    def test_sucet_float(self):
        calculator = Calculator()
        vysledok = calculator.sucet(2.5, 3.5)
        self.assertEqual(vysledok, 6)

    def test_sucet_negativny(self):
        calculator = Calculator()
        vysledok = calculator.sucet(-3, -5)
        self.assertEqual(vysledok, -8)

    def test_odvesna(self):
        calculator = Calculator()
        vysledok = calculator.sucet(4.24, 3)
        self.assertEqual(vysledok, 3)

    def test_korene_kvadratickej(self):
        calculator = Calculator()
        vysledok = calculator.korene_kvadratickej(1, 4, 3)
        self.assertEqual(vysledok, (-1, -3))


        
if __name__ == '__main__':
    unittest.main()

