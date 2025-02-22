from abc import ABC, abstractmethod
from model.chunking_model import ChunkingInput
from typing import List
class Chunking (ABC):
    def __init__(self, input_data: ChunkingInput):
        """
        Initialize the Chunking class.
        
        Parameters
        input_data : ChunkingInput
        The input data containing the text to be chunked.
        """
        self.text = input_data.text
    @abstractmethod 
    def chunk(self) -> List[str]:
        pass