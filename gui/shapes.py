import math

from turtle import Turtle, forward, left, right


t = Turtle()
t.speed(0)
t.hideturtle()


def polyline(n: int, length: int, angle: int) -> None:
    for _ in range(n):
        forward(length)
        left(angle)


def polygon(sides: int, size: int) -> None:
    angle = 360 / sides
    polyline(sides, size, angle)


def square(size: int) -> None:
    polygon(4, size)


def parallelogram(base: int, height: int, angle: int) -> None:
    for _ in range(2):
        forward(base)
        left(angle)
        forward(height)
        left(180 - angle)


def rectangle(length: int, width: int) -> None:
    parallelogram(length, width, 90)


def rhombus(size: int, angle: int) -> None:
    parallelogram(size, size, angle)


def arc(radius: int, angle: int) -> None:
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(n, step_length, step_angle)


def circle(radius: int) -> None:
    arc(radius, 360)


def koch(length: int) -> None:
    if length < 3:
        forward(length)
        return
    koch(length / 3)
    left(60)
    koch(length / 3)
    right(120)
    koch(length / 3)
    left(60)
    koch(length / 3)


if __name__ == "__main__":
    koch(120)
