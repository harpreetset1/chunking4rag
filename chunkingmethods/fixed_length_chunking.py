from model.chunking_model import ChunkingInput 
from chunkingmethods.base_chunking import Chunking

class FixedLengthChunking (Chunking):
    def __init__(self, input_data: ChunkingInput):
        """
        Initialize the FixedLengthChunking class.
        The FixedLengthChunking class is a concrete implementation of the Chunking interface.
        It divides the text into chunks of specified size.
        
        Parameters
        input_data: ChunkingInput
            The input data containing the text to be chunked.
        """
        super().__init__( input_data)
        self.chunk_size = input_data.chunk_size
        
    def chunk(self):
        """
        Divides the text into chunks of specified size.
        This method iterates over the text, creating a list of chunks 
        where each chunk is a substring of the text with a length equal 
        to the specified chunk size. The iteration stops when the end 
        of the text is reached.
        Returns
        List[str]
             A list of text chunks.
        """
        chunks = []
        for i in range(0, len(self.text), self.chunk_size):
            chunk = self.text[i:i + self.chunk_size]
            chunks.append (chunk)
            if i + self.chunk_size > len(self.text):
                break
        return chunks