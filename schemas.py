from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from database.models import UserRole, OrderChannel, OrderStatus

#Pydantic Schema
#Auth
class UserCreate(BaseModel):
    full_name : str
    email : EmailStr
    password : str = Field(min_length=6)
    role : UserRole

class LoginRequest(BaseModel):
    email : EmailStr
    password : str
    
#Product
class ProductResponse(BaseModel):
    id: int
    name : str
    price : float
    available : bool
    
    class config:
        orm_mode = True
        
class OrderItemAdd(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

#Order
class OrderCreate(BaseModel):
    channel: OrderChannel
    items : List[OrderItemAdd] = Field(min_items=1)
    
class OrderStatus(BaseModel):
    status : OrderStatus