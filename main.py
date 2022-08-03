from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def tim_forward():
    tim.forward(10)


def tim_backward():
    tim.backward(10)


def tim_counter_clockwise():
    tim.left(10)


def tim_clockwise():
    tim.right(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=tim_forward)
screen.onkey(key="s", fun=tim_backward)
screen.onkey(key="a", fun=tim_counter_clockwise)
screen.onkey(key="d", fun=tim_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
