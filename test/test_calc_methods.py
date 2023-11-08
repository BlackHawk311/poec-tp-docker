import unittest
from unittest import TestCase
from src.calc import apply_vat


class TestApplyVat(TestCase):

    def test1(self):
        print("Start test 1")
        new_price = apply_vat(100, 20)
        self.assertEqual(new_price, 120)
        print("End test 1")

    def test2(self):
        print("Start test 2")
        new_price = apply_vat(55.25, 5.5)
        self.assertEqual(new_price, 58.28874999999999)
        print("End test 2")

    def test3(self):
        print("Start test 3")
        new_price = apply_vat(0, 10)
        self.assertEqual(new_price, "The price ($ 0) is inferior or equal to 0.")
        print("End test 3")

    def test4(self):
        print("Start test 4")
        new_price = apply_vat(-10.99, 10)
        self.assertEqual(new_price, "The price ($ -10.99) is inferior or equal to 0.")
        print("End test 4")

    def test5(self):
        print("Start test 5")
        new_price = apply_vat("wrong value", 5.5)
        self.assertEqual(new_price, "ValueError: could not convert string to float: 'wrong value'")
        print("End test 5")

    def test6(self):
        print("Start test 6")
        new_price = apply_vat(100, -10)
        self.assertEqual(new_price, "The percentage (-10) is inferior or equal to 0.")
        print("End test 6")

    def test7(self):
        print("Start test 7")
        new_price = apply_vat(100, 110)
        self.assertEqual(new_price, "The percentage (110) is superior to 100.")
        print("End test 7")


if __name__ == '__main__':
    unittest.main()
