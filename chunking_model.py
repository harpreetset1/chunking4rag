from pydantic import BaseModel, Field 
from typing import List, Dict

class Metadata(BaseModel) :
    start_size: int 
    step_size: int 
    incremental: bool = Field(default=False, incremental=True)
class GraphNode(BaseModel) :
    start: int 
    end: int
    
class ChunkingInput (BaseModel) :
    text: str
    chunk_size: int = Field(None, description="Chunk size for overlap chunking")
    overlap_size: int = Field(None, description="Overlap size for overlap chunking")
    metadata: List[Metadata] = Field(default_factory=list, description="Metadata for metadata chunking")
    graph: List[GraphNode] = Field(default_factory=list, description="Graph nodes for graph-based chunking")