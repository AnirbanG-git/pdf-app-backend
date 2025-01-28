from pydantic import BaseModel
from typing import Optional

class PDFRequest(BaseModel):
    name: Optional[str] = None
    selected: Optional[bool] = None
    file: Optional[str] = None

class PDFResponse(BaseModel):
    id: int
    name: str
    selected: bool
    file: str

    class Config:
        from_attributes = True