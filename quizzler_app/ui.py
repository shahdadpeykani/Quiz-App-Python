from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canva = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canva.create_text(150, 125, width=280, text="Some questions", fill=THEME_COLOR,
                                                    font=("Arial", 20, "italic"))

        self.canva.grid(column=0, row=1, columnspan=2, pady=50)

        true_btn = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_btn, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_btn = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_btn, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text, text=q_text)
        else:
            self.canva.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):

        if is_right:
            self.canva.config(bg="green")

        else:
            self.canva.config(bg="red")

        self.window.after(1000, self.get_next_question)
