from fastapi import HTTPException, status
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
import jwt

#PWD setting:
password_hash = PasswordHash((Argon2Hasher(),))

SECRET_KEY = "test"
ALGORITHM = "HS256"
ACCESS_TIME_TOKEN = 30

def get_password(password: str):
    return password_hash.hash(password)

def verify_password(password: str, password_hased: str):
    return password_hash.verify(password, password_hased)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TIME_TOKEN)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired!")
    
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token denied!")