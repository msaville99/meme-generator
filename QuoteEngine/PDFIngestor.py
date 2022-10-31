"""PDFIngestor Package."""

from typing import List
import os
import random
import subprocess

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDFIngestor strategy object implements IngestorInterface."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class PDFIngestor parse method using pdftotext subprocess."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'

        try:
            subprocess.call(['pdftotext', '-layout', path, tmp])
        except Exception as err:
            print(f'ERROR: "{err}" executing pdftotext for {path}.')

        with open(tmp, 'r', encoding="utf-8") as file:
            quotes = []
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    new_quote = QuoteModel(parsed[0].strip(),
                                           parsed[1].strip())
                    quotes.append(new_quote)
        os.remove(tmp)

        return quotes
