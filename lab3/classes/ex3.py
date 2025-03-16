class Shape:
    def __init__(self):
        self.name = "shape"
        
    def area(self):
        return 0
    
class rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.name = "rectangle"
    def area(self):
         print(f"Area of {self.name}: {self.length * self.width}")
r = rectangle(4, 5)
r.area()