import math

g = float(input("Input the acceleration due to gravity: "))
yo = float(input("Input height of the barrel in meters: "))
x = float(input("Input horizontal distance in meters: "))
deg = float(input("Input angle of barrel in degrees: "))
theta = deg * math.pi / 180
vo = float(input("Input initial velocity: "))

answer = yo + x * math.tan(theta) - (g * x**2) / (2 * (vo * math.cos(theta)) ** 2)

print("The height of the projectile is", answer, "meters")