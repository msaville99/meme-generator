# meme-generator

## Overview
---
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

Performs the following functions:
- Loads quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).  
- Loads, manipulates, and save images.
- Accepts dynamic user input through a command-line tool and a web service. 

## Setup
---
Uses Python virtual environments to freeze module requirements in a reusable package. 

Execute in a terminal window to install dependencies:
```sh
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
```

To start the flask server, run:
```sh
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
```


## Description
---
Uses Object-oriented design in Python, including inheritence, abstract classes, class methods, and static methods.

### Quote Engine module

The Quote Engine module is responsible for ingesting many types of files that contain quotes. The Quote Model class encapsulates the body and author.

#### Ingestors
An abstract base class, IngestorInterface defines two methods with the following class method signatures:

```
def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
```
#### Strategy Objects

Separate strategy objects realizes IngestorInterface for each file type (csv, docx, pdf, txt).

#### Encapsulation

A final Ingestor class realizes the IngestorInterface abstract base class and encapsulates the helper classes. It implements logic to select the appropriate helper for a given file based on filetype.

### Meme Engine Module

The Meme Engine Module is responsible for manipulating and drawing text onto images. 

#### Meme Generator CLI
```
$ python3 meme.py --help
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

(Optional) Enter specific meme image path, quote text and author.

options:
  -h, --help       show this help message and exit
  --path PATH      where is the meme image file?
  --body BODY      what is the text of the quote?
  --author AUTHOR  who is the person of the quote?
  ```

#### Meme Generator Page
http://127.0.0.1:3000/
