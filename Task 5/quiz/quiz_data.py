# Quiz questions and answers
import random
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Jupiter", "Mars", "Saturn", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
        "answer": "Blue Whale"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    # Add more questions here...
    # ...

    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Au", "Gd", "Ag"],
        "answer": "Au"
    },
    {
        "question": "What is the world's longest river?",
        "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "Nile River"
    },
    {
        "question": "Which country is known as the 'Land of Thunder Dragon'?",
        "options": ["Bhutan", "Nepal", "Tibet", "Mongolia"],
        "answer": "Bhutan"
    },
    {
        "question": "Who wrote the famous novel 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "J.K. Rowling", "George Orwell", "J.R.R. Tolkien"],
        "answer": "Harper Lee"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    # ...

]


# Shuffle the answer options randomly for each question
for question in quiz_data:
    random.shuffle(question["options"])
