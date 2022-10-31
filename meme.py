"""Public module meme.py."""

import argparse
import os
import random

from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine.MemeEngine import MemeEngine

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    try:
        os.mkdir('./tmp')
    except OSError:
        pass
    try:
        os.mkdir('./static')
    except OSError:
        pass

    quote_files = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = './_data/photos/dog/'
    imgs = []

    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


def generate_meme(path=None, body=None, author=None):
    """Call Meme Generator."""
    img = None
    quote = None
    quotes, imgs = setup()

    if path is None:
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == '__main__':
    ARGS = None
    parser = argparse.ArgumentParser(
        description='(Optional) Enter specific meme image path,' +
                    'quote text and author.')
    parser.add_argument('--path', type=str,
                        help='where is the meme image file?')
    parser.add_argument('--body', type=str,
                        help='what is the text of the quote?')
    parser.add_argument('--author', type=str,
                        help='who is the person of the quote?')

    ARGS = parser.parse_args()
    print(generate_meme(ARGS.path, ARGS.body, ARGS.author))
