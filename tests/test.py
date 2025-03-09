
from data_extraction.document_parser import BaseDocumentType
from chunkingmethods.sentence_chunking import SentenceChunking
from chunkingmodel.chunking_model import ChunkingInput


from chunkingmethods.sentence_chunking import SentenceChunking
from chunkingmodel.chunking_model import ChunkingInput


text_content = "<html><body><p>Sample text content. This is a test. It has multiple sentences. It also has some punctuation.</p></body></html>"


text_document = BaseDocumentType(doc_type={"kind":"HTMLDocument"}).doc_type
content = text_document.get_content(text_content).pages[0].textual_content
data = ChunkingInput(
            text=content,
            )
sentence_chunking = SentenceChunking(data)
chunks = sentence_chunking.chunk()
print(chunks)

# for pdf document data extraction use the following
pdf_document = BaseDocumentType(doc_type={"kind":"PDFDocument"}).doc_type
with open("test.pdf", "rb") as f:
    extracted_content = pdf_document.get_content(f.read()).pages[0].textual_content
print(extracted_content)
