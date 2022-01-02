import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import User as ModelUser
from schema import User as SchemaUser
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Important commands
# You must be in the directory with a docker-compose.yml file
# docker-compose up -d
# To make a new db table
# 1) write the model
# 2) docker-compose run web alembic revision --autogenerate -m "Describe the table or change here" 
# Finally make the new table:
# 3) docker-compose run web alembic upgrade head 
# You can see the containers by typing:
# docker-compose ps 
# You can go backwards (remove tables using e.g.)
# docker-compose run web alembic downgrade -1  
# or
# docker-compose run web alembic downgrade -2
# Stop the containers with
# docker-compose stop           
# Remove them with 
# docker-compose rm                                                                                                                                           
