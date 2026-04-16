import math

def rectangle_area(width, height):
    return width*height

def rectangle_perimeter(width, height):
    return (width+height)*2

def circle_area(radius):
    if radius <= 0:
        return 'Radius can only be positive'
    return math.pi*(radius**2)

def circle_perimeter(radius):
    if radius <= 0:
        return 'Radius can only be positive'
    return math.pi*2*radius

def triangle_area(base, height):
    return base*height/2


