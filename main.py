#DataBase
from database.db_settings import Base, engine, get_db

#API
from fastapi import FastAPI

#Routes
from routes import users

#Start DataBase
Base.metadata.create_all(engine)
get_db()

#API
api = FastAPI()

#Test Endpoint
@api.get("/")
def read_root():
    return {"Hello": "World"}

#Conneting Routes
api.include_router(users.router)