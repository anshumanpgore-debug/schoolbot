from flask import Flask, render_template, request
import random

app = Flask(__name__)

# MAIN QUESTION-ANSWER DATABASE
school_questions = {
    # Greetings
    "hi": ["Hello! 😊", "Hi there! 👋", "Hey! How can I help you?"],
    "hello": ["Hello! 😊", "Hi! Welcome to SchoolBot 🤖"],
    "good morning": ["Good morning 🌞", "Good morning! Have a great day!"],
    "good night": ["Good night 🌙", "Sleep well 😴"],

    # Bot info
    "your name": ["My name is SchoolBot 🤖"],
    "who are you": ["I am SchoolBot 🤖, your school assistant."],
    "what can you do": ["I can help you with homework, school questions, exams, timetable, and more! 📚"],

    # School info
    "podar": ["Podar International School is a famous school in India with great education system."],
    "my school": ["Your school is Podar International School 🏫"],
    "principal": ["You can check the principal name from your school notice board or official website."],
    "school timing": ["School timings are usually morning to afternoon. Check your timetable for exact time."],

    # Subjects
    "math": ["Math is about numbers, logic, algebra, geometry, and problem solving."],
    "science": ["Science explains nature, physics, chemistry, biology, and experiments."],
    "english": ["English helps you improve grammar, writing, speaking, and reading skills."],
    "history": ["History teaches us about past events and civilizations."],
    "geography": ["Geography teaches about Earth, maps, climate, and environment."],
    "computer": ["Computer is an electronic device that processes data and gives output."],

    # Homework help
    "homework": ["Tell me your subject and question, I will help you 😊"],
    "assignment": ["Sure! Send your assignment question."],
    "project": ["Tell me your project topic, I will give you full project help."],

    # Exam related
    "exam": ["For exams, revise daily, solve sample papers, and practice writing."],
    "study tips": ["Study tips: Make timetable, revise daily, practice writing, and take breaks."],
    "timetable": ["Make timetable: 1 hour study + 10 min break. Focus on weak subjects first."],

    # Motivation
    "motivate me": ["You can do it 💪🔥 Keep studying and never give up!"],
    "i am tired": ["Take a small break, drink water, and start again 😊"],
    "i am stressed": ["Relax 😌 Take deep breaths and study step by step."],

    # School rules
    "uniform": ["Uniform is important in school because it creates discipline."],
    "discipline": ["Discipline helps students become responsible and successful."],
    "punishment": ["Punishment is not good, but rules are needed for discipline."],

    # General knowledge
    "capital of india": ["The capital of India is New Delhi 🇮🇳"],
    "national animal": ["National animal of India is Tiger 🐅"],
    "national bird": ["National bird of India is Peacock 🦚"],
    "largest planet": ["Largest planet is Jupiter 🌍"],
    "smallest planet": ["Smallest planet is Mercury ☄️"],
    "sun is a": ["Sun is a star ⭐"],

    # Fun
    "joke": ["Why did the student eat his homework? Because the teacher said it was a piece of cake! 😂"],
    "fun fact": ["Fun fact: Octopus has 3 hearts 🐙"],
    "story": ["Once upon a time… 😄 Tell me what type of story you want!"],

    # Bye
    "bye": ["Goodbye 👋 Have a nice day!", "Bye! Study well 📚"],
    "goodbye": ["Goodbye! See you soon 👋"],
}

# EXTRA SMART TOPIC ANSWERS (if keyword present)
keyword_answers = {
    "physics": "Physics is the study of motion, energy, force, light, and electricity.",
    "chemistry": "Chemistry is the study of substances, reactions, atoms, and molecules.",
    "biology": "Biology is the study of living organisms like plants and animals.",
    "algebra": "Algebra deals with variables like x and y and equations.",
    "geometry": "Geometry is about shapes, angles, triangles, circles, and area.",
    "fraction": "Fractions represent part of a whole. Example: 1/2 means half.",
    "percentage": "Percentage means out of 100. Example: 50% means 50 out of 100.",
    "photosynthesis": "Photosynthesis is the process by which plants make food using sunlight.",
    "electricity": "Electricity is the flow of electric charge through a conductor.",
    "forest": "Forest is an ecosystem with many trees and animals. It gives oxygen and maintains climate.",
    "pollution": "Pollution is harmful substances in air, water, or land.",
    "global warming": "Global warming is the rise in Earth’s temperature due to greenhouse gases.",
}

# DEFAULT replies
default_replies = [
    "Sorry, I didn’t understand 😅 Please ask a school-related question.",
    "Hmm… can you ask that in a simpler way? 😊",
    "I am not sure about that. Try asking about homework, exams, or subjects 📚",
]

def chatbot_reply(msg):
    msg = msg.lower().strip()

    # Exact match questions
    for question in school_questions:
        if question in msg:
            return random.choice(school_questions[question])

    # Keyword-based replies
    for key in keyword_answers:
        if key in msg:
            return keyword_answers[key]

    return random.choice(default_replies)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_msg = request.form["message"]
        reply = chatbot_reply(user_msg)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
