##DEFINES DATABASE TABLES
from sqlalchemy import Column, Integer, String
from ..database.connection import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    website = Column(String)