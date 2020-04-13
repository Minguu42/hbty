import unittest

from hbty.drawer import check_color


class CheckColorTest(unittest.TestCase):
    def test_specified_color(self):
        actual = check_color('red')
        self.assertEqual(actual, (255, 0, 0, 0))


if __name__ == '__main__':
    unittest.main()
