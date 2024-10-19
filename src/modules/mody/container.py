# src/modules/mody/container.py
from dependency_injector import containers, providers
from src.modules.mody.service import ModYService

class ModYContainer(containers.DeclarativeContainer):
    mody_service = providers.Singleton(ModYService)
