import unittest

from click.testing import CliRunner


class CliTest(unittest.TestCase):
    def test_cli(self):
        from hbty.core import cli
        runner = CliRunner()
        result = runner.invoke(cli, ['sky'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.stdout, '画像を作成しました。\n')


class BirthdayCardGeneratorTest(unittest.TestCase):
    def test_birthday_card_generator(self):
        from hbty.core import birthday_card_generate
        self.assertIsNone(birthday_card_generate('./sky.png', 'red', 'jun'))

    # TODO:画像を生成するかテストを書く


if __name__ == '__main__':
    unittest.main()
