from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db_settings import get_db
from database.models import User
from schemas import LoginRequest, UserCreate
from security import create_access_token, verify_password, get_password

router = APIRouter()

@router.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == req.email).first()
    password_validation = verify_password(req.password, user.password)
    if not user or not password_validation:
        raise HTTPException(status_code=401, detail="Email or password incorrect!")
    
    token = create_access_token(data={"sub": str(user.id)})
    return {"access token": token, "token type": "baerer"}

@router.post("/singin")
def signin(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")
    
    new_user = User(
        full_name = user.full_name,
        email = user.email,
        password = get_password(user.password),
        role = user.role
    )
    
    db.add(new_user)
    db.commit()
    
    return {"message": "User registered!"}