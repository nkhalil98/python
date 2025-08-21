import math

from turtle import Turtle, forward, left


t = Turtle()
t.speed(0)
t.hideturtle()


def draw_polyline(n: int, length: int, angle: int) -> None:
    for _ in range(n):
        forward(length)
        left(angle)


def draw_polygon(sides: int, size: int) -> None:
    angle = 360 / sides
    draw_polyline(sides, size, angle)


def draw_square(size: int) -> None:
    draw_polygon(4, size)


def draw_parallelogram(base: int, height: int) -> None:
    for _ in range(2):
        forward(base)
        left(60)
        forward(height)
        left(120)


def draw_rectangle(length: int, width: int) -> None:
    for _ in range(2):
        forward(length)
        left(90)
        forward(width)
        left(90)


def draw_arc(radius: int, angle: int) -> None:
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    draw_polyline(n, step_length, step_angle)


def draw_circle(radius: int) -> None:
    draw_arc(radius, 360)


if __name__ == "__main__":
    draw_circle(120)
