from typing import List

from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
