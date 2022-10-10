import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(ValueError):
            calc.calc(-1.0, -1.0)

    def test_case_2(self):
        self.assertEqual(calc.calc(3.0, 3.0), 'F')

    def test_case_3(self):
        self.assertEqual(calc.calc(4.0, 4.0), 'D')

    def test_case_4(self):
        self.assertEqual(calc.calc(6.0, 6.0), 'C')

    def test_case_5(self):
        self.assertEqual(calc.calc(7.0, 7.0), 'B')

    def test_case_6(self):
        self.assertEqual(calc.calc(9.0, 9.0), 'A')

if __name__ == '__main__':
    unittest.main()