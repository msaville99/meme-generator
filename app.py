import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    '''Load all resources'''

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = './_data/photos/dog/'
    imgs = []

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    '''Generate a random meme'''

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    '''User input for meme information'''
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    '''Create a user defined meme'''

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    if image_url is None:
        try:
            r = requests.get(image_url)
        except Exception as e:
            print(f'Exception error was {e}')

    tmp = f'./tmp/{random.randint(0,100000000)}.jpg'
    with open(tmp, 'wb') as img:
        img.write(r.content)

    if body is None:
        quote = random.choice(quotes)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(tmp, quote.body, quote.author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == '__main__':
    app.run(debug=True)
