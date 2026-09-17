from pydantic import BaseModel
from typing import Optional, List, Dict

class Card(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None