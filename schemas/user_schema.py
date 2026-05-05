from pydantic import BaseModel
from typing import Optional, List

#Pydantic Schema
class UserCreate(BaseModel):
    full_name : str
    email : str
    
class UserResponse(BaseModel):
    id : int
    full_name : str
    email : str