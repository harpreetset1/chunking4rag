from chunkingmethods.base_chunking import Chunking
from model.chunking_model import ChunkingInput

class OverlapChunking (Chunking):
    def __init__ (self, input_data: ChunkingInput):
        """
        Initialize the OverlapChunking class.
        Parameters
        input _data : ChunkingInput
        The input data containing the text to be chunked.
        """
        super().__init__(input_data)
        self.chunk_size = input_data.chunk_size
        self.overlap_size = input_data.overlap_size

    def chunk(self):
        """
        Divides the text into overlapping chunks of specified size.
        This method iterates over the text, creating a list of chunks where each 
        chunk is a substring of the text with a length equal to the specified chunk size 
        and an overlap of the specified overlap size. The iteration stops when the end of the text is reached.
        Returns
            List[str]
            A list of overlapping text chunks.
        """
        chunks = []
        for i in range(0, len(self.text), self.chunk_size- self.overlap_size):
            # Calculate the end position of the chunk
            chunk = self.text[i:i+ self. chunk_size]
            chunks.append (chunk)
            if (i + self. chunk_size - self.overlap_size) >= len(self.text):
                break
        return chunks
