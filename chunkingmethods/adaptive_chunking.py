from chunkingmethods.fixed_length_chunking import Chunking
from model.chunking_model import ChunkingInput

class AdaptiveChunking (Chunking):
    def __init__(self, input_data: ChunkingInput):
        """
        Initialize the AdaptiveChunking class.
        Parameters
        input_datä : ChunkingInput
        The input data containing the text to be chunked and the metadata for chunking.
        """
        super().__init__(input_data)
        if(input_data.metadata is None):
            raise ValueError("Metadata is required for adaptive chunking")
        self.metadata = input_data.metadata
    def chunk(self) :
        """
        Divides the text into chunks using the provided metadata and adaptive chunking strategy:
        This method iterates over the metadata, creating a list of chunks where each chunk is a 
        substring of the text with the start and end positions specified in the metadata. 
        The iteration stops when the end of the metadata is reached.
        The adaptive chunking strategy is implemented by creating chunks incrementally or 
        decrementally based on the passed size.
        Returns
        List[str]
        A list of text chunks.
        """
        chunks = []
        current_size = self.metadata.start_size
        i = 0
        while i < len (self.text):
            chunk = self.text[i:i + current_size]
            chunks.append(chunk)
            i += current_size
            if self.metadata.incremental:
                current_size += self.metadata.step_size
            else:
                current_size = max(self.metadata.start_size, current_size - self.metadata.step_size) 
        
        return chunks