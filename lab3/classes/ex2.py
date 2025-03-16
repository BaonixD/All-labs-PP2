class Shape:
    def __init__(self):
        self.name = "shape"
        
    def area(self):
        return 0
    
class square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.name = "square"

    def area(self):
        return self.length ** 2
s = square(9)
print(f"Shape name: {s.name}")
print(f"Area of square: {s.area()}")
