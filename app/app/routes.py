from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Question, Answer, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/quiz')
def quiz():
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@main.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    answers = request.form
    personality_scores = {'extrovert': 0, 'introvert': 0, 'analytical': 0}

    for q_id, a_id in answers.items():
        answer = Answer.query.get(a_id)
        personality_scores[answer.personality_type] += 1

    dominant_personality = max(personality_scores, key=personality_scores.get)
    return render_template('result.html', result=dominant_personality)
