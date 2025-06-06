import random

questions = [
    "Tell me about a time you handled conflict.",
    "Why do you want this job?",
    "Describe a challenge you've faced.",
    "What are your strengths and weaknesses?"
]

def get_random_question():
    return random.choice(questions)
