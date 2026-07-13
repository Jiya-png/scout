from fastapi import APIRouter

from .schema import ResearchRequest
from .service import ResearchService

router = APIRouter()

service = ResearchService()


@router.post("/research")
def research_company(request: ResearchRequest):
    return service.research(request.website)