import turtle
import pandas

file = pandas.read_csv("./28_States.csv")
screen = turtle.Screen()
picture = "./Webp.net-resizeimage.gif"
screen.addshape(picture)
turtle.shape(picture)
screen.title("Indian States Guessing Game")
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

all_states = file["state"].tolist()

correct_guess = 0
correct_answer = []

while correct_guess < 28:
    user_input = screen.textinput(title=f"Score {correct_guess}/28", prompt="Enter the next state ").title()

    if user_input == "Exit":
        break

    if user_input in all_states:
        x_pos = int(file[file.state == user_input]["x"])
        y_pos = int(file[file.state == user_input]["y"])
        turtle.goto(x_pos, y_pos)
        turtle.write(arg=f"{user_input}", align="center", font=("Arial", 8, "normal"))
        correct_guess += 1
        correct_answer.append(user_input)

not_able_to_guess = [answer for answer in all_states if answer not in correct_answer]

df = pandas.DataFrame(not_able_to_guess, columns=["These are all the states that you were not able to guess"])

df.to_csv("Incomplete_states.csv")

with open("./Incomplete_states.csv", 'a') as final:
    final.write(f"In total you were able to guess {correct_guess}/28 states")
