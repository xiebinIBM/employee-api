from sqlalchemy import Column, Integer, String, Date, Enum
from app.database import Base

class Employee(Base):
    __tablename__ = "employee"
    id          = Column(Integer, primary_key=True, index=True)
    emp_no      = Column(String(20), unique=True, index=True, nullable=False)
    name        = Column(String(50), nullable=False)
    department  = Column(String(50), nullable=False)
    gender      = Column(Enum("男", "女"), nullable=False)
    hire_date   = Column(Date, nullable=False)