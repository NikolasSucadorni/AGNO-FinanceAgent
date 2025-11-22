from agno.memory import Memory


class MemoryService:

    def __init__(self):
        self.memory = Memory()

    def get_memory(self):
        return self.memory
