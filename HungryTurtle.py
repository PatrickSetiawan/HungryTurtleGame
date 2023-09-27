# Python game developed for Junior Engineers curriculum, run through the steps below and make sure to comment every function
import turtle
import math
import random

# Display background
wn = turtle.Screen()
wn.bgcolor("blue")

# Draw screen border
pen = turtle.Turtle()
pen.penup()
border_size = 300
pen.setposition(-border_size,-border_size)
pen.speed(7)
pen.pendown()
pen.pensize(3)
for side in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()

# Create the player and define its appearance
player = turtle.Turtle()
player.color("lightgreen")
player.shape("turtle")
player.shapesize(1.5, 1.5, 0)
player.speed(0)

# penup() erases the trail that is left behind the turtle
player.penup()

# Turtle food (serves as the goal)
food = turtle.Turtle()
food.color("yellow")
food.shape("circle")
food.shapesize(0.5, 0.5, 0)
food.penup()
food.speed(0)
food.setposition(-100, -100)

# Set Speed variable
speed = 1

# Define movement functions
turn_speed = 30

def turn_left():
    player.left(turn_speed)

def turn_right():
    player.right(turn_speed)

def increase_speed():
    global speed
    speed += 1

# Bind keyboard to functions
# listen()
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")


while True:
    player.forward(speed)

    # Boundary collision, if player exceeds the border, bounce the player back
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    # Code for collision, don't need to explain all the nitty gritty of this code to students,
    # if they don't fully get how it works, it's fine. Just make sure they understand the concept
    # of coordinates.

    # This code basically uses the pythagorean theorem to find the distance between turtle and food
    distance_to_food = math.sqrt(math.pow(player.xcor()-food.xcor(), 2) + math.pow(player.ycor()-food.ycor(), 2))

    
    # when the turtl's and food's distance is below the threshold, set the food to appear in another location. The 25 is the offset so that food
    # doesn't randomly spawn in the edge of the border
    if distance_to_food < 20:
        food.setposition(random.randint(-border_size + 25, border_size - 25), random.randint(-border_size + 25, border_size - 25))
