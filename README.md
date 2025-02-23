# chunking4rag
This repo will have various chunking strategies one can build in order to get best performance out of RAG framework
The strategies discussed in this repo are:
1. [Fixed length chunking](./chunkingmethods/fixed_length_chunking.py)
  
2. [Keyword chunking](./chunkingmethods/keyword_chunking.py)
  
3. [Adaptive chunking](./chunkingmethods/adaptive_chunking.py)
  
4. [Sliding window](./chunkingmethods/sliding_window_chunking.py)
    
5. [Paragraph chunking](./chunkingmethods/paragraph_chunking.py)
  
6. [Sentence chunking](./chunkingmethods/sentence_chunking.py)
  
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