"""UNIT TESTS!!!!!!!"""
import unittest

# Pip install the src packages locally as dev/editable instead of relative import?
# Or add src to this module's search directory with sys?
from src.donut_package.example import *
from src.donut_package.module2 import *

class TestClass(unittest.TestCase):
    """First test case class"""

    # def setUp(self) -> None:
    #    return super().setUp()
    
    # @classmethod
    # def setUpClass(cls) -> None:
    #    return super().setUpClass()
    
    def test_adder(self):
        a = Adder()
        c = a.get_config()
        s = c['DEFAULT']['ServerAliveInterval']
        res = int(s)
        self.assertEqual(res, 45)

    # def test_single(self):
    #     pass

    # def test_bulk_neg(self):
    #     pass

if __name__ == '__main__':
    unittest.main()