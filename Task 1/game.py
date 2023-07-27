import tkinter as tk
from tkinter import ttk, messagebox
import random
from ttkthemes import ThemedTk

# Quiz questions and answers (add more questions as desired)
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["a) London", "b) Paris", "c) Rome", "d) Berlin"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Jupiter", "b) Mars", "c) Saturn", "d) Venus"],
        "answer": "b"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Lion"],
        "answer": "b"
    }
    # Add more questions here...
]


def load_quiz_questions():
    return random.sample(quiz_data, len(quiz_data))


class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.current_question = 0
        self.score = 0

        self.questions = load_quiz_questions()
        self.total_questions = len(self.questions)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TRadiobutton", font=("Helvetica", 10))
        self.style.configure("TButton", font=("Helvetica", 10))

        self.question_label = ttk.Label(root, text="", wraplength=400)
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
            root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.next_button = ttk.Button(
            root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question < self.total_questions:
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.radio_buttons[i].config(text=question_data["options"][i])
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.show_final_results()

    def submit_answer(self):
        selected_answer = self.answer_var.get()
        if selected_answer == self.questions[self.current_question]["answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Correct Answer!")
        else:
            correct_answer = self.questions[self.current_question]["answer"]
            messagebox.showinfo(
                "Incorrect", f"Incorrect Answer! The correct answer is: {correct_answer.upper()}")

        self.next_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)

    def next_question(self):
        self.current_question += 1
        self.display_question()

    def show_final_results(self):
        percentage = (self.score / self.total_questions) * 100
        messagebox.showinfo(
            "Quiz Results", f"You scored {self.score}/{self.total_questions} ({percentage:.2f}%)")
        self.root.destroy()


def main():
    root = ThemedTk(theme="clam")
    app = QuizGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
