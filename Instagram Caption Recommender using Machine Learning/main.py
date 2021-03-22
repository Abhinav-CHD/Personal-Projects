from tkinter import *
from tkinter import filedialog
import cv2
from captions import *
from random import choice
import pyperclip

FILE_PATH = None

base = Tk()
base.config(pady=50)
base.title("Instagram Caption Recommender")

# Create a canvas
img = PhotoImage(file="new.png")
canvas = Canvas()
canvas.create_image(200, 125, image=img)
canvas.grid(row=0, column=1)


# Function for opening the file

def file_opener():
    global FILE_PATH
    temp = filedialog.askopenfile(initialdir="/")
    FILE_PATH = str(temp.name)
    base.destroy()


# Button label
x = Button(text='Select an Image', command=file_opener)
x.grid(row=1, column=1)
mainloop()

if FILE_PATH == None:
    print("No Image was selected")
else:

    imagePath = FILE_PATH
    cascPath = './haarcascade_frontalface_default.xml'

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.7,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if len(faces) == 0:
        print("No Face was found!!")
    else:
        cv2.imshow("Faces found", image)
        cv2.waitKey(0)
        if len(faces) == 1:
            print(f"{len(faces)} Face Found")
            quote = choice(solo)
            print(quote)
            pyperclip.copy(quote)
        elif len(faces) == 2:
            print(f"{len(faces)} Face Found")
            quote = choice(best_friend)
            print(quote)
            pyperclip.copy(quote)
        else:
            print(f"{len(faces)} Face Found")
            quote = choice(group)
            print(quote)
            pyperclip.copy(quote)
