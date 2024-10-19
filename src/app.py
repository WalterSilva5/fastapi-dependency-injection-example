# src/app.py
from fastapi import FastAPI
from src.modules.modx.controller import router as modx_controller
from src.modules.mody.controller import router as mody_controller

from src.modules.core.containers import init_resources

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_resources()
    
@app.on_event("shutdown")
async def shutdown_event():
    pass

app.include_router(modx_controller, prefix="/modx")
app.include_router(mody_controller, prefix="/mody")
