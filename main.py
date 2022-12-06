from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race: red, orange, yellow, "
                                                           "green, blue, purple? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [150, 100, 50, 0, -50,-100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"The winner is the {winning_turtle} turtle. You win!")
            else:
                print(f"The winner is the {winning_turtle} turtle. You lose!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()