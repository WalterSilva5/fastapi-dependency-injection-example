from fastapi import Depends
from src.modules.request_counter.request_counter import (
    RequestsCounter,
)
from src.containers import Container


container = Container()


class RequestsCounterDependency:
    def __call__(
        self,
        requests_counter: RequestsCounter = Depends(
            lambda: Container.requests_counter()
        ),
    ):
        requests_counter.increment()
        return requests_counter

requests_counter_dependency = RequestsCounterDependency()
