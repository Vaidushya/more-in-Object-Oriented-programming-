# -- Homework -- #

class circle:
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        return 3.14 * (self.radius) ** 2

    def circle_circumference(self):
        return 2 * 3.14 * (self.radius)

print("\nEnter radius of circle for area calculation: ")
r = float(input())

print("\nEnter radius of circle for perimeter calculation: ")
r1 = float(input())

new_circle = circle(r)
print(f"\nArea of circle is: {new_circle.circle_area()}")

new_circle1 = circle(r1)
print(f"\nCircumference of circle is: {new_circle1.circle_circumference()}\n")
