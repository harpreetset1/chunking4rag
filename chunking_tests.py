import unittest
from chunkingmethods.sentence_chunking import SentenceChunking
from model.chunking_model import ChunkingInput, Metadata
from chunkingmethods.fixed_length_chunking import FixedLengthChunking
from chunkingmethods.sliding_window_chunking import OverlapChunking
from chunkingmethods.adaptive_chunking import AdaptiveChunking

class TestChunking(unittest.TestCase):

    def setUp(self):
        self.input_data = ChunkingInput(
            text="This is a test text to chunk.",
            chunk_size=5,
            overlap_size=2,
            metadata=None  # Assuming metadata is optional for the test
        )

    def test_fixed_length_chunking(self):
        base_chunking = FixedLengthChunking(self.input_data)
        chunks = base_chunking.chunk()
        expected_chunks = ["This ", "is a ", "test ", "text ", "to ch", "unk."]
        self.assertEqual(chunks, expected_chunks)

    def test_sliding_window_chunking(self):
        overlap_chunking = OverlapChunking(self.input_data)
        chunks = overlap_chunking.chunk()
        expected_chunks = ['This ', 's is ', 's a t', ' test', 'st te', 'text ', 't to ', 'o chu', 'hunk.', 'k.']
        self.assertEqual(chunks, expected_chunks)

    
    def test_sentence_chunking(self):
        sentence_chunking = SentenceChunking(self.input_data)
        chunks = sentence_chunking.chunk()
        expected_chunks = ["This is a test text to chunk."]
        self.assertEqual(chunks, expected_chunks)

if __name__ == '__main__':
    unittest.main()

