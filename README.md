# chunking4rag
For implementing a good RAG framework, we need 3 steps:
1. Data Ingestion/ Parsing
2. Chunking
3. Embedding/ Vectorization

Data Ingestion is a important steps where we extract data from a document. Aa document can be available in various formats like text, pdf, excel, csv or even Images. The data_extraction folder contains classes to extract data from different types of documents.

Chunking is the process of breaking up a document into smaller chunks. The chunking methods are implemented in the chunkingmethods folder.

The strategies discussed in this repo are:
1. [Fixed length chunking](./chunkingmethods/fixed_length_chunking.py)
  
2. [Keyword chunking](./chunkingmethods/keyword_chunking.py)
  
3. [Adaptive chunking](./chunkingmethods/adaptive_chunking.py)
  
4. [Sliding window](./chunkingmethods/sliding_window_chunking.py)
    
5. [Paragraph chunking](./chunkingmethods/paragraph_chunking.py)
  
6. [Sentence chunking](./chunkingmethods/sentence_chunking.py)

Embedding is the process of converting text into vectors. The embedding methods are implemented in the embeddingmethods folder.
  
# To use the library
The library is quite simple to use. Below example uses sentence chunking by extraction from text data

```python


from data_extraction.document_parser import DocumentParser
from chunkingmethods.sentence_chunking import SentenceChunking
from chunkingmodel.chunking_model import ChunkingInput


text_content = "<html><body><p>Sample text content. This is a test. It has multiple sentences. It also has some punctuation.</p></body></html>"


text_document = DocumentParser(doc_type={"kind":"HTMLDocument"}).doc_type
content = text_document.get_content(text_content).pages[0].textual_content
data = ChunkingInput(text=content)

sentence_chunking = SentenceChunking(data)
chunks = sentence_chunking.chunk()
print(chunks)

# for pdf document data extraction use the following
pdf_document = DocumentParser(doc_type={"kind":"PDFDocument"}).doc_type
with open("test.pdf", "rb") as f:
    extracted_content = pdf_document.get_content(f.read()).pages[0].textual_content
print(extracted_content)



```

# To install this library
Run the following command
```
pip install chunking4rag
```

# To start with contribution to the project
1. Clone the repository using git
  
2. Create a virtual environment using uv
  ```
  uv create chunking4rag
  ```
3. Activate the virtual environment
  ```
  source .venv/bin/activate
  ```
4. Install the dependencies by running
  ```
  uv install -r requirements.txt
  ```
5. Run tests to make sure everything is working fine
  ```
  python chuking_tests.py
  ```
