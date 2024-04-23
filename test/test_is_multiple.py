import unittest
from is_multiple import is_multiple_3_5

# RED - create and watch fail

# Green - create and watch pass

# Refactor - improve the code


class IsMultiple(unittest.TestCase):
    def test_recives_str_assertionError(self):
        with self.assertRaises(AssertionError):
            is_multiple_3_5('a')

    def test_return_multiple_3_5(self):
        payloads = (15, 30, 45, 60)
        response = 'Multiple 3 and 5!'

        for payload in payloads:
            with self.subTest(payload=payload, response=response):
                self.assertEqual(is_multiple_3_5(payload), response)

    def test_return_fail(self):
        payloads = (16, 31, 44)
        response = 'Fail!'

        for payload in payloads:
            with self.subTest(payload=payload, response=response):
                self.assertEqual(is_multiple_3_5(payload), response)

    def test_return_multiple_3(self):
        payloads = (6, 21, 18)
        response = 'Multiple 3!'

        for payload in payloads:
            with self.subTest(payload=payload, response=response):
                self.assertEqual(is_multiple_3_5(payload), response)

    def test_return_multiple_5(self):
        payloads = (5, 10, 50)
        response = 'Multiple 5!'

        for payload in payloads:
            with self.subTest(payload=payload, response=response):
                self.assertEqual(is_multiple_3_5(payload), response)


unittest.main(verbosity=2)
