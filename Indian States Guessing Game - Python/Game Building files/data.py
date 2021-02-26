import turtle
import pandas

with open("./gistfile1.txt") as file:
    states_list = file.read().splitlines()

screen = turtle.Screen()
screen.title("Guess States")

picture = "Webp.net-resizeimage.gif"
screen.addshape(picture)
turtle.shape(picture)

mylist = []
final = []


def pos(x, y):
    print(x, y)
    mylist.append((x, y))


screen.onscreenclick(pos)
screen.mainloop()

for i in range(len(states_list)):
    final.append({"state": states_list[i], "x": mylist[i][0], "y": mylist[i][1]})
df = pandas.DataFrame(final)
df.to_csv("28_States.csv")
