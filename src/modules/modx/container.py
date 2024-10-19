# src/modules/modx/container.py
from dependency_injector import containers, providers
from src.modules.modx.service import ModXService

class ModXContainer(containers.DeclarativeContainer):
    modx_service = providers.Singleton(ModXService)
