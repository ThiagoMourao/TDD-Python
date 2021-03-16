import unittest
from calculator import sum

class TestCalculator(unittest.TestCase):
    def test_5_sum_5_return_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_5_negative_and_5_return_0(self):
        self.assertEqual(sum(-5, 5), 0)

    def test_sum_multiple_various(self):
        x_y_returns =(
            (10, 10, 20),
            (1.5, 3.1, 4.6),
            (-5, 10, 5),
            (10, -10, 0),
        )

        for x_y_return in x_y_returns:
            with self.subTest(x_y_return=x_y_return):
                x, y, returnn = x_y_return
                self.assertEqual(sum(x, y), returnn)

    def test_sum_x_not_int_or_float_have_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum('assertionError', 0)

    def test_sum_y_not_int_or_float_have_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum('assertionError', 0)

if __name__ =='__main__':
    unittest.main(verbosity=2)