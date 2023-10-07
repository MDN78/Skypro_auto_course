
class Asserts:
    
    def __init__(self, color, result):
        self.color = color
        self.result = result
        assert self.color == self.result, "wrong color"
