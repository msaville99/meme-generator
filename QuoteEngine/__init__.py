"""QuoteEngine Module Initialization.

The Quote Engine module is responsible for ingesting
many types of files that contain quotes.
"""

from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .Ingestor import Ingestor
from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor
