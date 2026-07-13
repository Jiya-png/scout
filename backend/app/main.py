##STARTS THE APPLICATI
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .research.controller import router as research_router
from .database.connection import Base, engine, get_db
from .company.model import Company
from .company.schema import CompanyCreate, CompanyResponse
from .company.repository import create_company, get_companies

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(research_router)

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