import math

print("=========================\n", "Area Calculator 📐\n", "=========================")

print(" 1) Triangle\n",
      "2) Parallelogram\n",
      "3) Rectangle\n",
      "4) Square\n",
      "5) Cube\n",
      "6) Circle\n",
      "7) Sphere\n",
      "8) Quit\n")

shape = int(input("Choose a shape or quit: "))
print()

#~~~~~~~~~ triangle = shape 1 ~~~~~~~~~
if shape == 1:
    base = float(input("Base: "))  #base = int(input("Base: "))
    height = float(input("Height: "))  #height = int(input("Height: "))
    area = round((height * base) / 2, 2)
    print()
    print(f"The area of shape {shape} is: {area}")

#~~~~~~~~~ parallelogram = shape 2 ~~~~~~~~~
elif  shape == 2:
    base = float(input("Base: "))  #base = int(input("Base: "))
    vertical_height = float(input("Height: "))  #vertical_height = int(input("Height: "))
    area = round((vertical_height * base), 2)
    print()
    print(f"The area of shape {shape} is: {area}")

#~~~~~~~~~ rectangle = shape 3 ~~~~~~~~~
elif shape == 3:
    length = float(input("Length: ")) # length = int(input("Length: "))
    width = float(input("Width: ")) # width = int(input("Width: "))
    area = round(length * width, 2)
    print()
    print(f"The area of shape {shape} is: {area}")

#~~~~~~~~~ square = shape 4 ~~~~~~~~~
elif shape == 4:
    side = float(input("Side: ")) # side = int(input("Side: "))
    area = round(side ** 2, 2)
    print()
    print(f"The area of shape {shape} is: {area}")

#~~~~~~~~~ cube = shape 5 ~~~~~~~~~
elif shape == 5:
    edge = float(input("Length of Edge: ")) # edge = int(input("Length of Edge: "))
    area = round(6 * edge ** 2, 2)
    print()
    print(f"The area of shape {shape} is: {area}")

#~~~~~~~~~ circle = shape 6 ~~~~~~~~~
elif shape == 6:
    radius = float(input("Radius: ")) # radius = int(input("Radius: "))
    area = round(math.pi * radius ** 2, 2)
    print()
    print(f"The area of shape {shape} is: {area}")

#~~~~~~~~~ sphere = shape 7 ~~~~~~~~~
elif shape == 7:
    radius = float(input("Radius: ")) # radius = int(input("Radius: "))
    area = round(4 * math.pi * radius ** 2, 2)
    print()
    print(f"The area of shape {shape} is: {area}")

# ~~~~~~~~~ bye = 8 ~~~~~~~~~
else:
    print("\x1b[38;5;81m", "Byeeeeee ✌️", end="")
