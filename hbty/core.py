import click


@click.command()
def cli():
    """バースデーカード作成ツール"""
    birthday_card_generate()
    click.echo('動作確認')


def birthday_card_generate():
    pass
