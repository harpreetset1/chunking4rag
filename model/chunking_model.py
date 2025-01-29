from pydantic import BaseModel, Field 
from typing import Optional

class Metadata(BaseModel) :
    start_size: int 
    step_size: int 
    incremental: bool = Field(default=False)
    
class ChunkingInput(BaseModel):
    text: str
    chunk_size: int = Field(description="Chunk size for chunking",default=100)
    overlap_size: int = Field(description="Overlap size for chunking",default=20)
    metadata: Optional[Metadata] = Field(..., description="Metadata for chunking")
