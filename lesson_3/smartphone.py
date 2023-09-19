
class Smartphone():
    
    def __init__(self, mark, model, number):
        self.mark = mark
        self.model = model
        self.number = number

    def show_device(self):
        return f"{self.mark} - {self.model}. {self.number}"