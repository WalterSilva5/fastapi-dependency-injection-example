from fastapi import FastAPI
from src.modules.request_counter.controller import router as request_counter_router
from src.modules.health_check.controller import router as health_check_router

app = FastAPI()
app.include_router(request_counter_router)
app.include_router(health_check_router)