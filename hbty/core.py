import click


@click.command()
@click.option('--message', '-m', help='バースデーカードに乗せるメッセージ')
@click.option('-to', default='you', show_default=True,
              help='Happy Birthday to の後に入れる文字')
@click.argument('keyword')
def cli(keyword, message, to):
    """バースデーカード作成ツール"""
    birthday_card_generate(keyword, message, to)
    click.echo('動作確認')


def birthday_card_generate(keyword, message, to):
    pass
