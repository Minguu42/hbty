from hbty.drawer import save_with_message
from hbty.image_source import get_image

import click


@click.command()
@click.option('--message', '-m',
              default='MAY ALL YOUR DREAM COME TRUE THIS YEAR!!',
              help='バースデーカードに乗せるメッセージ')
@click.option('-to', default='YOU', show_default=True,
              help='Happy Birthday to の後に入れる文字')
@click.argument('keyword')
def cli(keyword, message, to):
    """バースデーカード作成ツール"""
    birthday_card_generate(keyword, message, to)
    click.echo('動作確認')


def birthday_card_generate(keyword, message, to):
    with get_image(keyword) as fp:
        save_with_message(fp, message, to)
