"""IngestorInterface Package."""

from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """IngestorInterface is an abstract base class.

    Defines two methods with the following class method signatures:

    def can_ingest(cls, path: str) -> boolean
    def parse(cls, path: str) -> List[QuoteModel]
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Return boolean if ingestor class can ingest file type."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse abstract method to be realized in helper classes."""
