from turtle import Shape


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Shape:
    def __init__(self, x: float, y: float, color: str):
        self.x = x
        self.y = y
        self.color = color

    def describe(self) -> str:
        return f"""
x:     {self.x} 
y:     {self.y}
color: {self.color}"""

    def distance(self, other: Point | Shape) -> float:
        if isinstance(other, Shape):
            pass

        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self) -> str:
        return f"Figure of the color {self.color} with center at point ({self.x}, {self.y})"


s1 = Shape(1, 2, "red")
s2 = Shape(2, 3, "blue")
print(s1.describe())
print(s2.describe())
print(s1.distance(s2))