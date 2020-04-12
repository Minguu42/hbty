from PIL import Image, ImageDraw, ImageFont

MAX_RATIO = 0.8

FONT_MAX_SIZE = 100
FONT_MIN_SIZE = 24

FONT_NAME = 'arial.ttf'
FONT_COLOR_WHITE = (255, 255, 255, 0)
FONT_COLOR_RED = (255, 0, 0, 0)

OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'


def save_with_message(fp, message, to):
    hbty = 'HAPPY'
    birthday = 'BIRTH DAY'
    to_you = 'TO ' + to + '!!'
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    font = ImageFont.truetype(FONT_NAME, 80)
    text_width, text_height = draw.textsize(
        hbty, font=font
    )

    hbty_position = (
    (image_width - text_width) / 2, (image_height - text_height) / 2 - 200)
    draw.text(hbty_position, hbty,
              fill=FONT_COLOR_WHITE, font=font)

    text_width, text_height = draw.textsize(
        birthday, font=font
    )
    birthday_position = (
    (image_width - text_width) / 2, (image_height - text_height) / 2 - 120)
    draw.text(birthday_position, birthday,
              fill=FONT_COLOR_WHITE, font=font)

    text_width, text_height = draw.textsize(
        to_you, font=font
    )
    to_you_position = (
    (image_width - text_width) / 2, (image_height - text_height) / 2 - 40)
    draw.text(to_you_position, to_you,
              fill=FONT_COLOR_WHITE, font=font)

    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
