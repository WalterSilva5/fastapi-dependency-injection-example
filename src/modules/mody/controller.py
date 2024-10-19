# src/modules/mody/controller.py
from fastapi import APIRouter, Depends
from src.modules.modx.container import ModXContainer
from src.modules.mody.container import ModYContainer

router = APIRouter()

@router.get("/mody")
def get_mody_count(
    modx_service = Depends(lambda: ModXContainer.modx_service()),
    mody_service = Depends(lambda: ModYContainer.mody_service())
):
    reqy = mody_service.increment() 
    reqx = modx_service.reqx
    return {"reqx": reqx, "reqy": reqy}
