from typing import List
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        with open(path, 'r') as file:
            for line in file:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-').strip()
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(new_quote)
        return quotes
