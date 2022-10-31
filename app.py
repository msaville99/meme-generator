"""Public module app.py."""

import random
import os
import requests
from flask import Flask, render_template, request

from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine.MemeEngine import MemeEngine

app = Flask(__name__)
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


@app.route('/')
def meme_rand():
    """Render a random meme."""
    quotes, imgs = setup()
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    if image_url is not None:
        try:
            req_img = requests.get(image_url, timeout=(5, 30), verify=False)
        except requests.exceptions.ConnectionError:
            return render_template('meme_error.html')

    tmp = f'./tmp/{random.randint(0, 100000000)}.jpg'
    with open(tmp, 'wb') as img:
        img.write(req_img.content)

    if body == '':
        quotes, _ = setup()
        quote = random.choice(quotes)
    else:
        if author == '':
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    path = meme.make_meme(tmp, quote.body, quote.author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == '__main__':
    app.run(debug=True)
