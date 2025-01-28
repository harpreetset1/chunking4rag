from nltk.tokenize import sent_tokenize
from chunkingmethods.base_chunking import Chunking
from model.chunking_model import ChunkingInput

class ParagraphChunking(Chunking):
    def __init__(self, input_data: ChunkingInput):
        super().__init__(input_data)

    def chunk(self):
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
