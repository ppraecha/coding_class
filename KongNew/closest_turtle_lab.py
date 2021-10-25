import turtle as tt
import random as r


def create_turtle(color, x=0, y=0, shape="turtle"):
    t = tt.Turtle()
    t.speed(0)
    t.shape(shape)
    t.color(color)
    t.penup()
    t.goto(x, y)
    return t


def distance(t1, t2):
    return abs(t2.xcor() - t1.xcor()) + abs(t2.ycor() - t1.ycor())


def travel(t1, t2):
    while t1.xcor() < t2.xcor():
        t1.forward(1)
    while t1.xcor() > t2.xcor():
        t1.backward(1)
    t1.left(90)
    while t1.ycor() < t2.ycor():
        t1.forward(1)
    while t1.ycor() > t2.ycor():
        t1.backward(1)
    t1.right(90)


tt.bgcolor("black")

# Create turtle and random position
main_tao = create_turtle("white")
main_tao.speed(50)
main_tao.pendown()
red_tao = create_turtle("red", r.randint(-200, 200), r.randint(-200, 200))
pp_tao = create_turtle("purple", r.randint(-200, 200), r.randint(-200, 200))
blue_tao = create_turtle("blue", r.randint(-200, 200), r.randint(-200, 200))

# Dict of unvisited turtle and the distance
unvisited = {
    red_tao: distance(main_tao, red_tao),
    pp_tao: distance(main_tao, pp_tao),
    blue_tao: distance(main_tao, blue_tao)
}

# While there are still unvisited turtle
while unvisited:
    # Get the closest turtle
    closest = min(unvisited, key=unvisited.get)
    # Travel to that turtle
    travel(main_tao, closest)
    # Remove the turtle from the unvisited list
    unvisited.pop(closest)
    # Update the distance between turtles
    for target in unvisited:
        unvisited[target] = distance(main_tao, target)

# Exit on click
tt.exitonclick()
