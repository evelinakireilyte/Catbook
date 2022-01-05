from pydantic import BaseModel
# from typing import List

from pydantic.networks import HttpUrl

class DocumentTypeBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class DocumentType(DocumentTypeBase):
    id: int

class DocumentBase(BaseModel):
    title: str
    position: int
    img: str

class Document(DocumentBase):
    id: int
    type_id: int
    type: DocumentTypeBase

    class Config:
        orm_mode = True 

