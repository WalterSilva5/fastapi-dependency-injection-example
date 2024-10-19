# src/modules/modx/service.py

class ModXService:
    def __init__(self):
        self.reqx = 0

    def increment(self):
        self.reqx += 1
        return self.reqx
