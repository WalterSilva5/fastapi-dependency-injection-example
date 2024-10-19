# src/modules/modx/controller.py
from fastapi import APIRouter, Depends
from src.modules.modx.container import ModXContainer
from src.modules.mody.container import ModYContainer

router = APIRouter()

@router.get("/modx")
def get_modx_count(
    modx_service = Depends(lambda: ModXContainer.modx_service()),
    mody_service = Depends(lambda: ModYContainer.mody_service())
):
    reqx = modx_service.increment()  # Incrementa o ModX
    reqy = mody_service.reqy  # Pega o valor atual do ModY
    return {"reqx": reqx, "reqy": reqy}