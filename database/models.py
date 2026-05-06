from sqlalchemy import Column, Integer, Float, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database.db_settings import Base
import enum

#DataBase Model
#User
class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)

#Product
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    available = Column(Boolean, default=True)

#ItemOrder
class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    
    order = relationship("Order", back_populates="items")

#Order
class OrderStatus(str, enum.Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    PAID = "PAID"
    
class OrderChannel(str, enum.Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    WEB = "WEB"
    SERVICE_COUNTER = "SERVICE_COUNTER"

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    channel = Column(Enum(OrderChannel), default=OrderChannel.WEB)
    status = Column(Enum(OrderStatus), default=OrderStatus.CREATED)
    
    items = relationship("OrderItem", back_populates="order")