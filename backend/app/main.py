##STARTS THE APPLICATI
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Company
from .schemas import CompanyCreate, CompanyResponse
from .crud import create_company, get_companies

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to Scout 🚀"
    }

@app.post("/companies", response_model=CompanyResponse)
def add_company(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):
    return create_company(db, company)


@app.get("/companies", response_model=list[CompanyResponse])
def list_companies(
    db: Session = Depends(get_db)
):
    return get_companies(db)