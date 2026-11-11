#this file to check linting pipeline
import math
 

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return math.pi * radius * radius


def calculate_circle_circumference(radius):
    return 2 * math.pi * radius


def greet_user(name):
    return f"Hello, {name}! Welcome to Python CI."


def main():
    radius = 5
    name = "DevOps Engineer"

    print(greet_user(name))
    print("Area:", calculate_area(radius))
    print("Circumference:", calculate_circle_circumference(radius))


if __name__ == "__main__":
    main()
