from flask import Flask, render_template, request, redirect, url_for, session
from data import get_question_data
from question_model import Question
from quiz_brain import QuizBrain

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    # Create Question objects
    question_data = get_question_data()
    question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]

    # Initialize QuizBrain
    quiz = QuizBrain(question_bank)

    # Save quiz state in session
    session['questions'] = [{"text": q.text, "answer": q.answer} for q in question_bank]
    session['question_number'] = 0
    session['score'] = 0

    return render_template('index.html')


@app.route('/question', methods=['GET', 'POST'])
def question():
    q_num = session.get('question_number', 0)
    questions = session.get('questions', [])

    if q_num >= len(questions):
        return redirect(url_for('result'))

    current_question = questions[q_num]

    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = current_question['answer']

        # Use QuizBrain check_answer
        quiz = QuizBrain([])  # dummy list
        quiz.score = session['score']
        quiz.question_number = session['question_number']

        quiz.check_answer(user_answer, correct_answer)

        session['score'] = quiz.score
        session['question_number'] = quiz.question_number + 1

        return redirect(url_for('question'))

    return render_template('question.html',
                           question=current_question,
                           q_num=q_num+1,
                           total=len(questions))


@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(session.get('questions', []))
    return render_template('result.html', score=score, total=total)


if __name__ == "__main__":
    app.run(debug=True)
