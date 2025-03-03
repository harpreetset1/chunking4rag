from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from chunkingmodel.document import Document, Page

class BaseDocumentType(BaseModel):
    """Class for storing a piece of text and associated metadata.

    
    """

    doc_type:TextDocument | PDFDocument | HTMLDocument | ImageDocument

            

class TextDocument(BaseModel):
    """Class for extracting a piece of text and associated metadata.

    Example:

        .. code-block:: python

            from core.documents import Document

            document = Document(
                doc_type={"kind":"TextDocument"}
            )
    """

    kind: Literal['TextDocument'] 
 
    def get_content(self, page_content: str) -> Document:
        """
        Retrieves the content of the HTML document.

        This method takes the content of the HTML document as a string and
        returns it as is.

        Parameters
        ----------
        page_content : str
            The content of the HTML document.

        Returns
        -------
        str
            The content of the HTML document.
        """
        p = Page(textual_content=page_content)
        return Document(pages=[p])
    
class HTMLDocument(BaseModel):
    """Class for extracting a piece of text data and associated metadata within html documents.

    Example:

        .. code-block:: python

            from core.documents import Document

            document = Document(
                doc_type={"kind":"HTMLDocument"}
            )
    """

    kind: Literal['HTMLDocument'] 
    


    def get_content(self, page_content: str, ignore_links: bool = True, ignore_images: bool = True) -> Document:
        """
        Convert HTML content to plain text.

        This method utilizes the html2text library to transform HTML content 
        into plain text format. The conversion process respects the specified
        settings for ignoring links and images.

        Parameters
        ----------
        page_content : str
            The HTML content to be converted.
        ignore_links : bool, optional
            If True, links in the HTML content will be ignored (default is True).
        ignore_images : bool, optional
            If True, images in the HTML content will be ignored (default is True).

        Returns
        -------
        str
            The converted plain text content.

        Raises
        ------
        ImportError
            If the html2text package is not installed.
        """
        try:
            import html2text
        except ImportError:
            raise ImportError(
                "html2text package not found, please install it with `pip install html2text`"
            )

        # Create a html2text.HTML2Text object and set properties
        h = html2text.HTML2Text()
        h.ignore_links = ignore_links
        h.ignore_images = ignore_images

        new_document = h.handle(page_content)
        p = Page(textual_content=new_document)
        return Document(pages=[p])
        

class PDFDocument(BaseModel):
    """Class for extracting a piece of text data and associated metadata within pdf documents.

    Example:

        .. code-block:: python

            from core.documents import Document

            document = Document(
                doc_type={"kind":"PDFDocument"}
            )
    """

    kind: Literal['PDFDocument']
    
    def get_content(self, page_content: bytes) -> Document:
        """
        Extract the text content from a PDF byte stream.

        This method uses the PyPDF2 library to extract the text content from the PDF byte stream
        and returns it as a string.

        Parameters
        ----------
        page_content : bytes
            The PDF content to extract the text from.

        Returns
        -------
        str
            The extracted text content.

        Raises
        ------
        ImportError
            If the PyPDF2 library is not installed.
        """

        try:
            from pypdf import PdfReader
            import io
        except ImportError:
            raise ImportError(
                """PyPDF2 package not found, please 
                install it with `pip install PyPDF2`"""
            )

        content = ""
        pages = []
        for page in PdfReader(io.BytesIO(page_content)).pages:
            content += page.extract_text()

            p = Page(textual_content=content)  
            pages.append(p)
        
        d = Document(pages=pages)  
        return d


class ImageDocument(BaseModel):
    """Class for extracting a piece of text data and associated metadata within image documents.

    Example:

        .. code-block:: python

            from core.documents import Document

            document = Document(
                doc_type={"kind":"PDFDocument"}
            )
    """

    kind: Literal['ImageDocument']
    
    def get_content(self, page_content: bytes) -> Document:
        """
        Extract the text content from an image byte stream using OCR.

        This method uses the pytesseract library to perform OCR on the image byte stream
        and returns the extracted text as a string.

        Parameters
        ----------
        page_content : bytes
            The image content to extract the text from.

        Returns
        -------
        str
            The extracted text content.

        Raises
        ------
        ImportError
            If the pytesseract or PIL library is not installed.
        """

        try:
            from PIL import Image
            import pytesseract
            import io
        except ImportError:
            raise ImportError(
                """pytesseract or PIL package not found, please 
                install them with `pip install pytesseract pillow`"""
            )

        image = Image.open(io.BytesIO(page_content))
        content = pytesseract.image_to_string(image)
        p = Page(textual_content=content)
        d = Document(pages=[p])
        return d

