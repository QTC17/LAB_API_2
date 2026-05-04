from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials, firestore 
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
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

class Note(BaseModel):
    user_email: str
    content: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/notes", response_model=List[Note])
async def get_notes():
    try:
        list_tu_firebase = []
        docs = db.collection("notes").stream()
        
        for doc in docs:
            list_tu_firebase.append(doc.to_dict())
            
        return list_tu_firebase 
        
    except Exception as e:
        print(f"Lỗi : {e}")
        return []

@app.post("/notes")
async def create_note(note: Note):
    try:
        db.collection("notes").document().set(note.dict())
        return {"status": "success", "data": note}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))