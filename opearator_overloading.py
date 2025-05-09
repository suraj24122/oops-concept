# Define a class 'point'
class point:
    # Constructor to initialize x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator to add two points
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)
    
    # Overloading the 'str()' method to print a point nicely
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Overloading the '==' operator to compare two points
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Create a point object p1 at (1, 2)
p1 = point(1, 2)

# Create a point object p2 at (2, 4)
p2 = point(2, 4)

# Add two points using overloaded '+' operator
p3 = p1 + p2

# Print the result of addition (prints (3, 6) using __str__)
print(p3)

# Compare p1 and p2 using overloaded '==' operator (prints False)
print(p1 == p2)
    