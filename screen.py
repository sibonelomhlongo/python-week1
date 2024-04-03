import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("X Snake Game")
screen.bgcolor("green")
screen.setup(width=800, height=800)
screen.tracer(0)  # Turn off automatic screen updates

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.goto(-300, 300)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.fd(580)
    border_pen.rt(90)
border_pen.hideturtle()

# Create the snake
snake = []
for _ in range(2):  # Initial length of the snake
    segment = turtle.Turtle()
    segment.speed(0)
    segment.shape("circle")
    segment.color("blue")
    segment.penup()
    snake.append(segment)

start_x = 0
start_y = 0
for segment in snake:
    segment.goto(start_x, start_y)
    start_x -= 20

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.goto(random.randint(-260, 260), random.randint(-260, 260))

# Main game loop
while True:
    screen.update()  # Update the screen manually

    # Move the snake
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    snake[0].forward(20)  # Move the head segment forward

    time.sleep(0.1)  # Control the speed of the snake movement

# Keep the window open
turtle.done()