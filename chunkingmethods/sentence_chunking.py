from chunkingmethods.base_chunking import Chunking
from chunkingdatamodel.chunking_model import ChunkingInput
from typing import List
from nltk.tokenize import sent_tokenize
import nltk


class SentenceChunking(Chunking):
    """
    A class that will break a textual input into chunks of sentences.

    Attributes:
        text (str): The input text to be chunked.
    """

    def __init__(self, input_data: ChunkingInput):
        """
        Initialize the SentenceChunking class.

        Parameters:
            input_data (ChunkingInput): The input data containing the text to be chunked.
        """
        super().__init__(input_data)
        self.text = input_data.text

    def chunk(self) -> List[str]:
        """
        Break a textual input into chunks of sentences.

        Returns:
            List[str]: A list of text chunks, where each chunk is a sentence.
        """
        nltk.download('punkt_tab')
        #sentences = self.text.split('. ')
        sentences = sent_tokenize(self.text)
        return sentences
