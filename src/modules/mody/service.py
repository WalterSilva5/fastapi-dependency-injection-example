# src/modules/mody/service.py
class ModYService:
    def __init__(self):
        self.reqy = 0

    def increment(self):
        self.reqy += 1
        return self.reqy
