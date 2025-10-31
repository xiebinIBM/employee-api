from fastapi import FastAPI
from app.database import engine, Base
from app.routers import employee
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Employee PoC API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee.router)

@app.get("/")
def root():
    return {"message": "employee poc api"}