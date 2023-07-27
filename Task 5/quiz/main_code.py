import tkinter as tk
from tkinter import ttk, messagebox
import random
from ttkthemes import ThemedTk
from quiz_data import quiz_data


class KBCQuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KBC Quiz Game")
        self.current_question = 0
        self.score = 0
        self.user_answers = {}  # To store user-selected answers

        self.questions = random.sample(quiz_data, len(quiz_data))
        self.total_questions = len(self.questions)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=(
            "Helvetica", 12), foreground="black")
        self.style.configure("TRadiobutton", font=(
            "Helvetica", 10), foreground="black")
        self.style.configure("TButton", font=(
            "Helvetica", 10), foreground="white", background="blue")

        self.question_label = ttk.Label(root, text="", wraplength=600)
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.answer_var.set(None)
        self.radio_buttons = []

        for i in range(4):
            radio_button = ttk.Radiobutton(
                root, text="", variable=self.answer_var, value=str(i))
            self.radio_buttons.append(radio_button)
            radio_button.pack(pady=5)

        self.submit_button = ttk.Button(
            root, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.next_button = ttk.Button(
            root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.feedback_label = ttk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question < self.total_questions:
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.radio_buttons[i].config(
                    text=question_data["options"][i], state=tk.NORMAL)
            self.submit_button.config(state=tk.NORMAL)
            self.feedback_label.config(text="")
        else:
            self.show_final_results()

    def submit_answer(self):
        selected_answer = self.answer_var.get()
        if selected_answer != "":
            self.radio_buttons[int(selected_answer)].config(state=tk.DISABLED)
            question_data = self.questions[self.current_question]
            correct_answer = question_data["answer"]
            if int(selected_answer) == question_data["options"].index(correct_answer):
                self.feedback_label.config(text="Correct!", foreground="green")
                self.score += 1
            else:
                self.feedback_label.config(
                    text=f"Wrong! Correct answer: {correct_answer}", foreground="red")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < self.total_questions:
            self.answer_var.set(None)
            self.display_question()
        else:
            self.next_button.config(state=tk.DISABLED)
            self.calculate_score()

    def calculate_score(self):
        percentage = (self.score / self.total_questions) * 100
        messagebox.showinfo(
            "KBC Quiz Results", f"You scored {self.score}/{self.total_questions} ({percentage:.2f}%)", parent=self.root)
        self.root.destroy()


def main():
    root = ThemedTk(theme="clam")
    app = KBCQuizGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
