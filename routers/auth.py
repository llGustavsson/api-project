from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db_settings import get_db
from database.models import User
from schemas import LoginRequest, UserCreate

router = APIRouter()

@router.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
     
    test_email = db.query(User).filter(User.email == req.email).first()
    test_password = db.query(User).filter(User.password == req.password).first()
    if not test_email or not test_password:
        raise HTTPException(status_code=401, detail="Email or password incorrect!")
    
    return {"message": "Access Permitted!"}

@router.post("/singin")
def signin(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")
    
    new_user = User(
        full_name = user.full_name,
        email = user.email,
        password = user.password,
        role = user.role
    )
    
    db.add(new_user)
    db.commit()
    
    return {"message": "User registered!"}