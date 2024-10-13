from fastapi import APIRouter, Depends
from src.modules.request_counter.request_counter import RequestsCounter, HealthCheckResponse
from src.modules.request_counter.dependency import requests_counter_dependency

router = APIRouter()

@router.get("/health-check", response_model=HealthCheckResponse)
def health_check(requests_counter: RequestsCounter = Depends(requests_counter_dependency)):
    return HealthCheckResponse(
        message="API is running smoothly.", request_count=requests_counter.get_count()
    )
