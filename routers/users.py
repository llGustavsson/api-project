from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db_settings import get_db
from database.models import User

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user

