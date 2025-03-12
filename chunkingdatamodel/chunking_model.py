from pydantic import BaseModel, Field 
from typing import Optional

    
class ChunkingInput(BaseModel):
    text: str
    chunk_size: Optional[int] = Field(description="Chunk size for chunking",default=100)
    overlap_size: Optional[int] = Field(description="Overlap size for chunking",default=20)
    file_path: Optional[str] = Field(description="File path for chunking",default="./")
    start_size: Optional[int] = Field(description="Start size for chunking",default=100) 
    step_size: Optional[int] = Field(description="Step size for chunking",default=10) #int 
    incremental: Optional[bool] = Field(description="Incremental for chunking",default=False)
    metadata: Optional[dict] = Field(description="Metadata for chunking", default=None)
