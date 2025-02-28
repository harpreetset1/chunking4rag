from abc import ABC, abstractmethod



class Embeddings(ABC):
    """Abstract class for embeddings.

    This class is used to define the interface for the different embeddings
    classes. It provides an abstract method to embed a list of text documents.

    Attributes:
        name (str): The name of the embeddings algorithm.
    """

    @abstractmethod
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed  docs.

        Args:
            texts: List of text to embed.

        Returns:
            List of embeddings.
        """

    
    