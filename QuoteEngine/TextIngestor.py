"""TextIngestor Package."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """TextIngestor strategy object implements IngestorInterface."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class TextIngestor parse method."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    new_quote = QuoteModel(
                                    parsed[0].strip(),
                                    parsed[1].strip())
                    quotes.append(new_quote)
        return quotes
