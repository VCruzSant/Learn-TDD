import unittest
from calculator import sum


class TestCalculator(unittest.TestCase):
    def test_sum_5_5_return_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_10_negative_10_return_0(self):
        self.assertEqual(sum(-10, 10), 0)

    def test_various_tests(self):
        x_y_exits = (
            (10, 20, 30),
            (55, 22, 77),
            (15, 15, 30),
            (1.3, 3.1, 4.4),
            (0, 0, 1)
        )

        for x_y_exit in x_y_exits:
            # assim eu consigo identificar qual parâmetro deu erro
            with self.subTest(x_y_exit=x_y_exit):
                x, y, exit = x_y_exit
                print(f'{x} + {y} = {exit}')

                self.assertEqual(sum(x, y), exit)

    def test_sum_x_not_int_return_assetion_error(self):
        with self.assertRaises(AssertionError):
            sum('1', 1)


unittest.main(verbosity=2)
