from typing import List,Optional
from pydantic import BaseModel

    
class Page(BaseModel):
    textual_content: str
    binary_content: Optional[bytes] = None
    image_content: Optional[List[bytes]] = None 
    tabular_content: Optional[List[List[str]]] = None 
    metadata: Optional[dict] = None
    
    def __str__(self) -> str:
        return self.textual_content
    
class Document(BaseModel):
    pages: List[Page]
