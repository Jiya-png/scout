##Defines what data comes into and goes out of the API.
from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    website: str


class CompanyResponse(CompanyCreate):
    id: int

    class Config:
        from_attributes = True