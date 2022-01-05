from typing import List
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import Document as ModelDocument
from schema import Document as SchemaDocument
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/documents/", response_model=SchemaDocument)
def create_document(document: SchemaDocument):
    db_document = ModelDocument(
        title=document.title, position=document.position, type_id=document.type_id
    )
    db.session.add(db_document)
    db.session.commit()
    return db_document

@app.get("/documents/", response_model=List[SchemaDocument])
def get_documents():
    documents = db.session.query(ModelDocument).all()
    return documents

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

