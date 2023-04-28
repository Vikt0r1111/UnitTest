from math import pi

def circle_area(radius):
    if type not in [int, float]:
        raise TypeError("Потрібні числа")
    if radius < 0:
        raise ValueError("Радіус неможу бути негативним числом")
    return pi*radius**2