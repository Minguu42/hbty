import random

from PIL import Image, ImageDraw, ImageFont

MAX_RATIO = 0.8

FONT_NAME = 'arial.ttf'

FONT_COLORS = {'white': (255, 255, 255, 0), 'red': (255, 0, 0, 0),
               'green': (0, 255, 0, 0), 'blue': (0, 0, 255, 0),
               'yellow': (255, 212, 0, 0)}

OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'


def save_with_message(fp, color, to):
    """画像にメッセージを載せて保存する"""
    happy = 'HAPPY'
    birthday = 'BIRTH DAY'
    to_you = 'TO ' + to + '!!'
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    text_draw(image, draw, happy, 200, color)
    text_draw(image, draw, birthday, 120, color)
    text_draw(image, draw, to_you, 40, color)

    image.save(OUTPUT_NAME, OUTPUT_FORMAT)


def text_draw(image, draw, text, height_position, color='random',
              font_size=80):
    """テキストを画像に描写する"""
    image_width, image_height = image.size

    font = ImageFont.truetype(FONT_NAME, font_size)
    text_width, text_height = draw.textsize(
        text, font=font
    )
    first_position = (
        (image_width - text_width) / 2,
        (image_height - text_height) / 2 - height_position)

    for i, char in enumerate(text):
        font_color = check_color(color)
        position = (first_position[0] + i * 50, first_position[1])
        draw.text(position, char, fill=font_color, font=font)


def check_color(color):
    """フォントの色の決定する"""
    if color.lower() in tuple(FONT_COLORS.keys()):
        return FONT_COLORS[color.lower()]
    else:
        return FONT_COLORS[random.choice(tuple(FONT_COLORS.keys()))]
