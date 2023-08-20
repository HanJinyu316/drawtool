import unittest
from back import back


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(back('9+3'), '9')  # add assertion here


if __name__ == '__main__':
    unittest.main()
