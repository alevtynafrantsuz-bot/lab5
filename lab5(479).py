import math
x = 0
y = 0
while True:
    line = input().strip()

    if line == "":
        break

    direction, steps = line.split()
    steps = int(steps)

    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps
distance = math.sqrt(x ** 2 + y ** 2)
print(round(distance))