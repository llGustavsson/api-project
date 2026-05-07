from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database.db_settings import get_db
from database.models import User
from security import decode_access_token

#URL token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_currrent_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    user_id : str = payload.get("sub")
    user = db.query(User).filter(User.id == int(user_id)).first()    
    
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    
    return user