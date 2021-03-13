from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Random Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0, command=self.pressed_true, bd=0,
                                  activebackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0)

        self.false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, command=self.pressed_false, bd=0,
                                   activebackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="active")
            self.false_button.config(state="active")

        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")

    def pressed_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def pressed_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
