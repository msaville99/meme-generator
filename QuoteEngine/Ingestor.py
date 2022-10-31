"""Ingestor Package."""

from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Implement the IngestorInterface ABC and encapsulate helper classes.

    Select the appropriate ingestor helper class for a given file based on
    filetype.
    """

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingestor parse class method.

        Determine correct ingester class to realize based on file type.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
