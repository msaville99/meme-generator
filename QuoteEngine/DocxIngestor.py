"""DocxIngestor Package."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """DocxIngestor Class strategy object implements IngestorInterface."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class DocxIngestor parse method using docx library."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                # print(para.text)
                parsed = para.text.split('-')
                new_quote = QuoteModel(parsed[0].strip(), parsed[1].strip())
                quotes.append(new_quote)

        return quotes
