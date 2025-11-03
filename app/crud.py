from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.models import Employee

def get_all(db: Session):
    return db.query(Employee).all()

def get_by_id(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

def get_by_query(db: Session, emp_no: str = None, name: str = None,
                 department: str = None, gender: str = None, hire_date: str = None):
    query = db.query(Employee)
    if emp_no:
        query = query.filter(or_(Employee.emp_no == emp_no, Employee.emp_no.contains(emp_no)))
    if name:
        query = query.filter(or_(Employee.name == name, Employee.name.contains(name)))
    if department:
        query = query.filter(or_(Employee.department == department, Employee.department.contains(department)))
    if gender:
        query = query.filter(Employee.gender == gender)
    if hire_date:
        query = query.filter(Employee.hire_date == hire_date)
        
    return query.all()

def create(db: Session, obj: EmployeeCreate):
    db_obj = Employee(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, emp_id: int, obj: EmployeeUpdate):
    db_obj = get_by_id(db, emp_id)
    for k, v in obj.dict().items():
        setattr(db_obj, k, v)
    db.commit()
    return db_obj

def delete(db: Session, emp_id: int):
    db_obj = get_by_id(db, emp_id)
    db.delete(db_obj)
    db.commit()
    return db_obj