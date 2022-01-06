# ----------------------------------------------------------------------------------------------------------------------
# gen_inv_num.py - Musée Bolo (c) by C. Gaudin - Generate Inventory Number
# ----------------------------------------------------------------------------------------------------------------------
from src.inventory_scripts.inventory_number import is_valid_inventory_number
from src.inventory_scripts.inventory_number import is_valid_inv_number_and_year
from src.inventory_scripts.inventory_number import get_year_and_number
from src.inventory_scripts.inventory_number import build_inventory_number
import unittest


class TestBoloInventoryNumber(unittest.TestCase):

    def test_valid_number(self):
        self.assertTrue(is_valid_inventory_number('2021-000-123'))
        self.assertTrue(is_valid_inventory_number('3023-034-123'))

    def test_invalid_number(self):
        self.assertFalse(is_valid_inventory_number('2021-000-1231'))
        self.assertFalse(is_valid_inventory_number('302O-034-123'))

    def test_padding(self):
        self.assertFalse(is_valid_inventory_number('2021-000-123 '))
        self.assertFalse(is_valid_inventory_number(' 2221-000-123'))

    def test_before_inventory(self):
        self.assertFalse(is_valid_inventory_number('1999-000-123'))

    def test_year_in_futur(self):
        self.assertFalse(is_valid_inv_number_and_year('2221-000-123'))

    def test_year_in_past(self):
        self.assertFalse(is_valid_inv_number_and_year('2019-000-123'))

    def test_year_valid(self):
        self.assertTrue(is_valid_inventory_number('2020-000-123'))

    def test_get_year_and_number(self):
        year, number = get_year_and_number('2020-011-123')
        self.assertEqual(2020, year)
        self.assertEqual(11123, number)

    def test_get_year_and_number_none(self):
        year, number = get_year_and_number('2020-011-12343')
        self.assertIsNone(year)
        self.assertIsNone(number)

    def test_generate(self):
        inventory_str = build_inventory_number(2020, 111222)
        self.assertEqual("2020-111-222", inventory_str)


if __name__ == '__main__':
    unittest.main()
