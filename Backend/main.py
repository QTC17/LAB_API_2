from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials
from pydantic import BaseModel
from typing import List

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

cred = credentials.Certificate("Backend/labapi2-firebase-adminsdk-fbsvc-c2d32c0c11.json") 
firebase_admin.initialize_app(cred)

class Note(BaseModel):
    user_email: str
    content: str

db_notes = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/notes", response_model=List[Note])
async def get_notes():
    return db_notes

@app.post("/notes")
async def create_note(note: Note):
    db_notes.append(note.dict())
    return {"status": "success", "data": note}