from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class DocumentType(Base):
    __tablename__ = "types"    
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    documents = relationship("Document", back_populates="type")

class Document(Base):
    __tablename__ = "documents"    
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    position = Column(String)
    img = Column(String)
    type_id = Column(Integer, ForeignKey("types.id"))
    
    type = relationship("DocumentType", back_populates="documents")