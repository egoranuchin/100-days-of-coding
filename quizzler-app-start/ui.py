from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label

        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)

        # Button

        true_button_image = PhotoImage(file="images/true.gif")
        false_button_image = PhotoImage(file="images/false.gif")

        self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.check_if_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_button_image, highlightthickness=0, command=self.check_if_false)
        self.false_button.grid(column=1, row=2)

        # Canvas

        self.question_canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            width=280,
            text="question prompt",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_if_true(self):
        # is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))

    def check_if_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


