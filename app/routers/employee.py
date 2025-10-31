from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import *
from app.schemas import *
from app.database import get_db
import logging

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/", response_model=list[EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    return get_all(db)

@router.post("/search", response_model=list[EmployeeOut])
def search_employees(
    emp_no: str = None,
    name: str = None,
    department: str = None,
    gender: str = None,
    hire_date: str = None,
    db: Session = Depends(get_db)
):
    logging.info(f"Received search parameters: emp_no={emp_no}, name={name}, department={department}, gender={gender}, hire_date={hire_date}")
    return get_by_query(db, emp_no, name, department, gender, hire_date)

@router.post("/", response_model=EmployeeOut)
def add_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return create(db, emp)

@router.put("/{emp_id}", response_model=EmployeeOut)
def edit_employee(emp_id: int, emp: EmployeeUpdate, db: Session = Depends(get_db)):
    return update(db, emp_id, emp)

@router.delete("/{emp_id}")
def remove_employee(emp_id: int, db: Session = Depends(get_db)):
    delete(db, emp_id)
    return {"ok": True}