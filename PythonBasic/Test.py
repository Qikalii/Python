import unittest
import sys


sys.path.append("F:\AppData\Git\Repository\Python\Function")


from TestFunction import my_adder
from TestFunction import ShoppingList


class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5, 3), 8)

    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5, 3), -2)


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 53)
