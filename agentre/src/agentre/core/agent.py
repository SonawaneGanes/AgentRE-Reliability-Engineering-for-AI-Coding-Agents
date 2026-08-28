"""Base agent abstractions."""

class Agent:
    def __init__(self, name, llm=None):
        self.name = name
        self.llm = llm
