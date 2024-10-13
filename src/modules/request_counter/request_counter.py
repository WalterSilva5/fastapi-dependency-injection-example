from pydantic import BaseModel

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

