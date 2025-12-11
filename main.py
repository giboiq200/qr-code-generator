from fastapi import FastAPI,HTTPException
from databaseConnection import db_connection
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from io import BytesIO
import qrcode
import sqlite3
import bcrypt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserProfile(BaseModel):
    username:str
    email:str
    password:str

@app.post("/register")
def register(user:UserProfile):
    con = db_connection()
    cursor = con.cursor()
    cursor.execute(""" SELECT * FROM users WHERE email=?
""",(user.email,))
    result = cursor.fetchone()
    if result is not None:
        con.close()
        return {"success": False, "error": "Email already exists"}
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    if result is None:
        cursor.execute(""" 
                       INSERT INTO users(name,email,password)
                       VALUES (?,?,?)
""",(user.username,user.email,hashed_password))
    con.commit()
    con.close()
    return {"success": True}

class QRRequest(BaseModel):
    url:str

@app.post("/generate_qr")
def generate(request:QRRequest):
    img = qrcode.make(request.url)
    buf = BytesIO()
    img.save(buf,format="PNG")
    buf.seek(0)
    return StreamingResponse(buf,media_type="image/png")

class UserLogin(BaseModel):
    email:str
    password:str

@app.post("/login")
def login(user: UserLogin):
    con = db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (user.email,))
    result = cursor.fetchone()
    
    if result is None:
        con.close()
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    stored_password_hash = result[3] 
    if not bcrypt.checkpw(user.password.encode('utf-8'), stored_password_hash):
        con.close()
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    con.close()
    return {"success": True}
