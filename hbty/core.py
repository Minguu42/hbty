from hbty.drawer import save_with_message
from hbty.image_source import get_image

import click


@click.command()
@click.option('--color', '-c',
              default='random',
              help='メッセージの色: white, red, blue, green, yellow')
@click.option('-to', default='YOU', show_default=True,
              help='Happy Birthday to の後に入れる文字')
@click.argument('keyword')
def cli(keyword, color, to):
    """バースデーカード作成ツール"""
    birthday_card_generate(keyword, color, to)
    click.echo('画像を作成しました。')


def birthday_card_generate(keyword, color, to):
    with get_image(keyword) as fp:
        save_with_message(fp, color, to)
