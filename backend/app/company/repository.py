##CRUD operations for the Company model.
#TALKS TO DATABASE AND PERFORMS CRUD OPERATIONS

from sqlalchemy.orm import Session
from .model import Company


def create_company(db: Session, company):
    db_company = Company(
        name=company.name,
        website=company.website
    )

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company


def get_companies(db: Session):
    return db.query(Company).all()