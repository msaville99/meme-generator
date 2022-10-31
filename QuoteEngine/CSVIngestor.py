"""CSVIngestor Package."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSVIngestor strategy object implements IngestorInterface."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class CSVIngestor parse method using pandas library."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for _, row in df.iterrows():
            # print(row)
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
