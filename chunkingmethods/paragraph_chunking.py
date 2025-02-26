from nltk.tokenize import sent_tokenize
from chunkingmethods.base_chunking import Chunking
from chunkingmodel.chunking_model import ChunkingInput
from typing import List
class ParagraphChunking(Chunking):
    def __init__(self, input_data: ChunkingInput):
        """
        Initialize the ParagraphChunking class.
        
        Parameters
        input_data: ChunkingInput
        The input data containing the text to be chunked.
        """
        super().__init__(input_data)
        self.text = input_data.text
        

    def chunk(self) -> List[str]:
        """
        Break a textual input into chunks of paragraphs.

        This method splits the input text into paragraphs. The paragraphs are separated by two or more
        consecutive newline characters. It then tokenizes each paragraph into sentences and stores them
        in a new list. The list of sentences is then returned as the chunks.

        Returns:
            List[str]: A list of text chunks, where each chunk is a paragraph.
        """
        paragraphs = []
        sentences = sent_tokenize(self.text)
        current_paragraph = ""
        for sentence in sentences:
            if sentence.strip() == "":
                if current_paragraph != "":
                    paragraphs.append(current_paragraph)
                    current_paragraph = ""
            else:
                current_paragraph += sentence + " "
        if current_paragraph != "":
            paragraphs.append(current_paragraph)
        return paragraphs
