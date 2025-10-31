from pydantic import BaseModel, Field
from datetime import date

class EmployeeBase(BaseModel):
    emp_no:     str = Field(..., max_length=20)
    name:       str = Field(..., max_length=50)
    department: str = Field(..., max_length=50)
    gender:     str = Field(..., pattern="^(男|女)$")
    hire_date:  date

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    class Config:
        from_attributes = True