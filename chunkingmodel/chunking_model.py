from pydantic import BaseModel, Field 
from typing import Optional

class Metadata(BaseModel) :
    start_size: int 
    step_size: int 
    incremental: bool = Field(default=False)
    
class ChunkingInput(BaseModel):
    text: str
    chunk_size: Optional[int] = Field(description="Chunk size for chunking",default=100)
    overlap_size: Optional[int] = Field(description="Overlap size for chunking",default=20)
    file_path: Optional[str] = Field(description="File path for chunking",default="./")
    metadata: Optional[Metadata] = Field(description="Metadata for chunking", default=None)
