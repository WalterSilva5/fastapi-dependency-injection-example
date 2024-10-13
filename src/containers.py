from dependency_injector import containers, providers
from src.modules.request_counter.request_counter import RequestsCounter


class Container(containers.DeclarativeContainer):
    requests_counter = providers.Singleton(RequestsCounter)

