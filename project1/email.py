import turtle
import time
import random
import csv
import time

def authenticate():
    while True:
        # Prompt the user to enter the password
        password = turtle.textinput("Snake Game", "Enter the password to start the game:")
        
        # Check if the password is correct
        if password == "Snake":
            print("Authentication successful!")
            return True
        else:
            print("Incorrect password. Please try again.")

# Authenticate the user before starting the game
if authenticate():
    delay = 0.1

    # Score
    def read_from_csv():
        values = []
        with open('highscore.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                values.append(int(row[0]))  # Convert to int and add to list
        return values
    try:
        val=read_from_csv()
        high_score=val[0]
    except Exception:
        print('error!:')
    score = 0

    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game by @X GROUP")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0) # Turns off the screen updates

    # Draw border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("red")
    border_pen.penup()
    border_pen.goto(-260, 250)
    border_pen.pendown()
    border_pen.pensize(5)
    for _ in range(4):
        border_pen.fd(500)
        border_pen.rt(90)
    border_pen.hideturtle()

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("white")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"
    increment=20

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("circle")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24))

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + increment)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - increment)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - increment)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + increment)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")

    # Function to pause the game
    def reset_game():
        global score
        
    # Keyboard bindings
    wn.listen()
   # wn.onkeypress(toggle_pause(), "p")  # Press "p" to pause/resume the game

    j=True
    # Main game loop
   
    while j:
        wn.update()

        # Check for a collision with the border
        if head.xcor()>220 or head.xcor()<-240 or head.ycor()>225 or head.ycor()<-222:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            with open('highscore.csv','w') as csvfile:
                csvfile.write(str(high_score))
            
            turtle.textinput("Game Over", "Try again? (yes/no)").lower()
            
            
            
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-239, 219)
            y = random.randint(-219, 224)
            food.goto(x,y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color("blue")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                with open('highscore.csv','w') as csvfile:
                    csvfile.write(str(high_score))
                # Hide the segments
                
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1
            
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
                #prompt player to play again or quit
        if score>=50:
            increment=25
        
        time.sleep(delay)


    wn.mainloop()