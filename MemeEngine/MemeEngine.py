"""MemeEngine Package."""

import os
from random import randint
from textwrap import TextWrapper

from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """MemeEngine Class."""

    def __init__(self, output_dir):
        """Initialize MemeEngine with output_dir path."""
        self.author = None
        self.img = None
        self.img_path = None
        self.output_dir = output_dir
        self.text = None
        self.width = None

        try:
            os.mkdir(self.output_dir)
        except OSError:
            pass

    def read_image(self):
        """Read image from file."""
        try:
            self.img = Image.open(self.img_path)
        except FileNotFoundError:
            print("File not found.")

    def resize_image(self):
        """Resize image."""
        if self.width is not None:
            ratio = self.width/float(self.img.size[0])
            height = int(ratio*float(self.img.size[1]))
            self.img.resize((self.width, height), Image.ANTIALIAS)

    def add_text(self):
        """Add randomly positioned text to image."""
        if (self.img is not None and
            self.text is not None and
                self.author is not None):
            draw = ImageDraw.Draw(self.img)
            font = ImageFont.truetype(
                    './fonts/IndieFlower-Regular.ttf',
                    size=20)

            wrapper = TextWrapper(width=30)
            text_filled = wrapper.fill(text=self.text)

            print(f'text_filled = {text_filled}')

            # Randomly select x-axis.
            rnd_x = randint(((self.img.size[0] * 20) // 100),
                            ((self.img.size[0] * 50) // 100))
            rnd_y = randint(((self.img.size[1] * 20) // 100),
                            ((self.img.size[1] * 80) // 100))

            draw.text(
                (rnd_x, rnd_y),
                f'"{text_filled}"\n\t\t\t- {self.author}',
                font=font,
                fill='red')

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Meme With a Text Quote.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the body of the quote.
            author {str} -- The author of the quote.
        Outputs:
            out_path -- the path to the saved output image file.
        """
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width
        out_path = f'{self.output_dir}/{os.path.basename(self.img_path)}'

        self.read_image()
        self.resize_image()
        self.add_text()

        self.img.save(out_path)
        return out_path
