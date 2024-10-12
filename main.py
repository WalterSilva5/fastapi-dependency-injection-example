from fastapi import FastAPI, Depends
from pydantic import BaseModel
from dependency_injector import containers, providers
import uvicorn


class RequestsCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


class RequestsCountResponse(BaseModel):
    count: int


class HealthCheckResponse(BaseModel):
    message: str
    request_count: int


class Container(containers.DeclarativeContainer):
    requests_counter = providers.Singleton(RequestsCounter)


def get_requests_counter(
    requests_counter: RequestsCounter = Depends(lambda: Container.requests_counter()),
):
    requests_counter.increment()
    return requests_counter


app = FastAPI()


@app.get("/requests_count", response_model=RequestsCountResponse)
def requests_count(requests_counter: RequestsCounter = Depends(get_requests_counter)):
    return RequestsCountResponse(count=requests_counter.get_count())


@app.get("/health_check", response_model=HealthCheckResponse)
def health_check(requests_counter: RequestsCounter = Depends(get_requests_counter)):
    return HealthCheckResponse(
        message="API is running smoothly.", request_count=requests_counter.get_count()
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
