# ==================
# Area Calculator 📐
# ==================

# 1) Triangle
# 2) Rectangle
# 3) Square
# 4) Circle
# 5) Quit

# Which shape: 1

# Base: 5
# Height: 6

# The area is 15

import math

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

shape = int(input("Which Shape: "))

if shape == 1:
    base = int(input("Base: "))
    height = int(input("Height: "))
    area = base * height / 2
    print(f"The area is {area}")
elif shape == 2:
    length = int(input("Length: "))
    width = int(input("Width: "))
    area = length * width
    print(f"The area is {area}")
elif shape == 3:
    side = int(input("Side: "))
    area = side ** 2
    print(f"The area is {area}")
elif shape == 4:
    radius = int(input("Radius: "))
    area = math.pi * radius ** 2
    print(f"The area is {area}")
else:
    print("See you next time!")