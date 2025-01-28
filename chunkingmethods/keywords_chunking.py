from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from chunkingmethods.base_chunking import Chunking
from model.chunking_model import ChunkingInput
class KeywordsChunking(Chunking):
    """
    A class that creates extracts keywords from input text and returns them as chunks.
    """
    def __init__(self, input_data: ChunkingInput):
        """
        Initialize the KeywordsChunking class.
        Parameters
        input_data : ChunkingInput
        The input data containing the text to be chunked.
        """
        super().__init__(input_data)
        self.stop_words = set(stopwords.words('english') + list(punctuation))

    def chunk(self):
        """
        Extracts keywords from input text and returns them as chunks.
        Returns
        List[str]
        A list of keywords extracted from the input text.
        """
        tokens = word_tokenize(self.text)
        keywords = [word for word in tokens if word.lower() not in self.stop_words]
        return keywords
