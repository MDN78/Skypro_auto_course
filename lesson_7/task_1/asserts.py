
class Asserts:
    
    def __init__(self, color: str, result: str) -> bool:
        """Checking colors"""
        self.color = color
        self.result = result
        assert self.color == self.result, "wrong color"
