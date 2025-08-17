class rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width
    
    def rectangle_perimeter(self):
        return 2*(self.length + self.width)
    
new_rectange = rectangle(12,10)
print(f"Area of rectangle is: {new_rectange.rectangle_area()}")

new_rectange1 = rectangle(5,8)
print(f"Perimeter of rectangle is: {new_rectange1.rectangle_perimeter()}")
