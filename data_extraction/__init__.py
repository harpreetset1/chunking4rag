
# You can import the core components of the chunking4rag package here
# so that they can be accessed directly from the core module

from data_extraction.document_parser import DcoumentParser, TextDocument, PDFDocument, HTMLDocument
from data_extraction.excel_parser import ExcelDocument
from data_extraction.image_parser import ImageDocument

__all__ = ["DcoumentParser", "TextDocument", "PDFDocument", "HTMLDocument", "ExcelDocument", "ImageDocument"]

