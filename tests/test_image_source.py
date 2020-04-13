import unittest

from hbty.image_source import LocalImage, RemoteImage
from hbty.image_source import KeywordImage, choose_image_source


class KeywordImageTest(unittest.TestCase):

    def test_build_url(self):
        actual = KeywordImage('sample')._build_url('sample')
        self.assertEqual(actual, 'https://loremflickr.com/800/600/sample')


if __name__ == '__main__':
    unittest.main()
