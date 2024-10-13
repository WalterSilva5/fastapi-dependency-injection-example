from src.modules.request_counter.request_counter import RequestsCounter, RequestsCountResponse
from src.modules.request_counter.dependency import requests_counter_dependency
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/requests_count", response_model=RequestsCountResponse)
def requests_count(requests_counter: RequestsCounter = Depends(requests_counter_dependency)):
    return RequestsCountResponse(count=requests_counter.get_count())

