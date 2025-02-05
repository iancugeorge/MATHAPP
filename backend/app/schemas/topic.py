# schemas/topic.py

from pydantic import BaseModel
from typing import List, Optional

class TopicCreate(BaseModel):
    name: str
    description: Optional[str] = None
    prerequisite_topics: Optional[List[int]] = None  # List of topic IDs that are prerequisites

class TopicResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    prerequisite_topics: Optional[List[int]] = None

    class Config:
        from_attributes = True
