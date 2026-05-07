from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db_settings import get_db
from database.models import Product
from schemas import ProductResponse
from typing import List

router = APIRouter()

@router.get("/menu", response_model=list[ProductResponse])
def show_menu(db: Session = Depends(get_db)):
     menu = db.query(Product).filter(Product.available == True).all()
     
     if not menu:
         raise HTTPException(status_code=401, detail="Out of stock!")
     
     return menu