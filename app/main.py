import os
import firebase_admin
import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from firebase_admin import credentials, initialize_app, db
from pydantic import BaseModel
from dotenv import load_dotenv

from routers import login

load_dotenv()

app = FastAPI()

db_certificate = os.getenv('FIREBASE_CERTIFICATE')


if not firebase_admin._apps:
    cred = credentials.Certificate(db_certificate)
    firebase_app = firebase_admin.initialize_app(cred)


app.include_router(login.login_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)



