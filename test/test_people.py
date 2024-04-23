import unittest
from unittest.mock import patch
from people import People


class TestPeople(unittest.TestCase):
    def setUp(self):
        self.p1 = People('Vini', 'Sant')

    def test_people_attr_name(self):
        self.assertEqual(self.p1.name, 'Vini')

    def test_people_attr_name_str(self):
        self.assertIsInstance(self.p1.name, str)

    def test_people_attr_surname(self):
        self.assertEqual(self.p1.surname, 'Sant')

    def test_people_attr_surname_str(self):
        self.assertIsInstance(self.p1.surname, str)

    def test_get_all_data_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'CONECTED')

    def test_get_all_data_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERROR 404')


if __name__ == '__main__':
    unittest.main(verbosity=2)
