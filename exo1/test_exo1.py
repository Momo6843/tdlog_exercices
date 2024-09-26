import unittest

from exo1 import item


class Exo1Test(unittest.TestCase):

    def test_item_construction(self):
        item = item(10, 20)

        self.assertEqual(20, item.weight)
