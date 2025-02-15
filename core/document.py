from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import PurePath
from typing import Any, Literal, Optional, Union

from pydantic import Field, field_validator


PathLike = Union[str, PurePath]


class BaseDocument(ABC):
    id: Optional[str] = None
    metadata: dict = Field(default_factory=dict)

    @field_validator("id", mode="before")
    def convert_id_to_str(cls, id_value: Any) -> Optional[str]:
        if id_value is not None:
            return str(id_value)
        else:
            return id_value
    @abstractmethod
    def get_page_content(self) -> Document:
        raise NotImplementedError

class Document(BaseDocument):
    """Class for storing a piece of text and associated metadata.

    Example:

        .. code-block:: python

            from chunking4rag.core.documents import Document

            document = Document(
                page_content="Hello, world!",
                metadata={"source": "https://example.com"}
            )
    """

    page_content: str
    type: Literal["Document"] = "Document"

    def __init__(self, page_content: str, **kwargs: Any) -> None:
        """Pass page_content in as positional or named arg."""
        # my-py is complaining that page_content is not defined on the base class.
        # Here, we're relying on pydantic base class to handle the validation.
        super().__init__(page_content=page_content, **kwargs)  # type: ignore[call-arg]

    @classmethod
    def get_document_namespace(cls) -> list[str]:
        """Get the namespace of the document."""
        return ["schema", "document"]

    def __str__(self) -> str:
        """Override __str__ to restrict it to page_content and metadata."""
        # The format matches pydantic format for __str__.
        #
        # The purpose of this change is to make sure that user code that
        # feeds Document objects directly into prompts remains unchanged
        # due to the addition of the id field (or any other fields in the future).
        #
        # This override will likely be removed in the future in favor of
        # a more general solution of formatting content directly inside the prompts.
        if self.metadata:
            return f"page_content='{self.page_content}' metadata={self.metadata}"
        else:
            return f"page_content='{self.page_content}'"
        
    def get_page_content(self) -> Document:
        return self   

class TextDocument(Document):
    """Class for storing a piece of text and associated metadata.

    Example:

        .. code-block:: python

            from chunking4rag.core.documents import TextDocument

            document = TextDocument(
                page_content="Hello, world!",
                metadata={"source": "https://example.com"}
            )
    """

    type: Literal["TextDocument"] = "TextDocument"
    def __init__(self, page_content: str, **kwargs: Any) -> None:
        """Pass page_content in as positional or named arg."""
        # my-py is complaining that page_content is not defined on the base class.
        # Here, we're relying on pydantic base class to handle the validation.
        super().__init__(page_content=page_content, **kwargs)  # type: ignore[call-arg]

    def get_page_content(self) -> Document:
        """
        Returns the current instance of the document.

        This method is used to retrieve the current instance of the Document object,
        which contains the page content and associated metadata.

        Returns
        -------
        Document
            The current instance of the Document.
        """

        return self
    
class HTMLDocument(Document):
    """Class for storing a piece of text data and associated metadata within html documents.

    Example:

        .. code-block:: python

            from chunking4rag.core.documents import HTMLDocument

            document = HTMLDocument(
                page_content=b'Hello, world!',
                metadata={"source": "https://example.com"}
            )
    """

    type: Literal["HTMLDocument"] = "HTMLDocument"
    page_content: str
    def __init__(self, page_content: str, ignore_links: bool = True, ignore_images: bool = True, **kwargs: Any) -> None:
        """
        Initialize the HTMLDocument instance with the given arguments.

        Parameters
        ----------
        page_content : str
            The HTML content to store in the document.
        ignore_links : bool, optional
            Whether to ignore links (a tags) in the text content. Defaults to True.
        ignore_images : bool, optional
            Whether to ignore images in the text content. Defaults to True.
        **kwargs
            Additional keyword arguments to pass to the base class constructor.
        """
        self.ignore_links = ignore_links
        self.ignore_images = ignore_images
        super().__init__(page_content=page_content, **kwargs)

    def get_page_content(self) -> Document:
        """
        Converts the HTML content stored in the document to plain text using the html2text library.

        This method initializes an HTML2Text object to convert the HTML content (`page_content`)
        to plain text while respecting the `ignore_links` and `ignore_images` settings.

        Returns
        -------
        Document
            A new Document instance containing the converted plain text and the existing metadata.

        Raises
        ------
        ImportError
            If the html2text package is not installed.
        """

        try:
            import html2text
        except ImportError:
            raise ImportError(
                """html2text package not found, please 
                install it with `pip install html2text`"""
            )

        # Create a html2text.HTML2Text object and override some properties
        h = html2text.HTML2Text()
        h.ignore_links = self.ignore_links
        h.ignore_images = self.ignore_images

        new_document = Document(
            page_content=h.handle(self.page_content), metadata={**self.metadata}
        )
            
        return new_document