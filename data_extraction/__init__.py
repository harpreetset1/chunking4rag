
# You can import the core components of the chunking4rag package here
# so that they can be accessed directly from the core module

from .document_parser import BaseDocumentType, TextDocument, PDFDocument, HTMLDocument

__all__ = ["BaseDocumentType", "TextDocument", "PDFDocument", "HTMLDocument"]

