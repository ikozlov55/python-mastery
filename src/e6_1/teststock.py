import unittest

from stock import Stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_kwargs(self):
        s = Stock(name='GOOG', price=490.1, shares=100)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, s.shares * s.price)

    def test_sell(self):
        shares = 100
        sell_count = 50
        s = Stock('GOOG', shares, 490.1)
        s.sell(sell_count)
        self.assertEqual(s.shares, shares - sell_count)

    def test_sell_all(self):
        shares = 100
        sell_count = 101
        s = Stock('GOOG', shares, 490.1)
        s.sell(sell_count)
        self.assertEqual(s.shares, 0)

    def test_from_row(self):
        s = Stock.from_row(['GOOG', '100', '490.1'])
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(repr(s), 'Stock(GOOG, 100, 490.1)')

    def test_eq(self):
        s1 = Stock('GOOG', 100, 490.1)
        s2 = Stock('GOOG', 100, 490.1)
        s3 = Stock('AAb', 100, 490.1)
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)

    def test_shares_as_str(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'

    def test_shares_as_negative(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -1

    def test_price_as_str(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '50.4'

    def test_price_as_negative(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -1.0

    def test_nonexistent_attr(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 60


if __name__ == '__main__':
    unittest.main()
