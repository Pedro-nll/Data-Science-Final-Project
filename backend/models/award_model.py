from typing import List, Optional
from pydantic import BaseModel

class Award(BaseModel):
    title: str
    year: Optional[int] = None
