import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/question/<int:question_id>')
def question(question_id):

    return render_template(
        'questions/'+str(question_id)+'.html')

@app.route('/error')
def error():
    return render_template(
        'error.html')

@app.route('/success')
def success():
    return render_template(
        'success.html')

@app.route('/about/<int:score>')
def about():
    return render_template(
        'about.html')

@app.route('/questions/<string:answer>/<int:question_id>')
def questions( answer, question_id ):
    try:
        score = 0
        if question_id == 1:
            question_id += 1
            if answer == "15th":
                score += 1
                return render_template(
                    'success.html',
                    next=question_id,
                    score=score)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="15th Amendment",
                    next=question_id)
        elif question_id == 2:
            question_id += 1
            if answer == "YOUR ANSWER HERE":
                score += 1
                return render_template(
                    'success.html',
                    next=question_id,
                    score=score)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="YOUR CORRECT ANSWERE HERE",
                    next=question_id)
        elif question_id == 4:
            question_id += 1
            if answer == "Rev":
                score += 1
                return render_template(
                    'success.html',
                    next=question_id,
                    score=score)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="The Revolution",
                    next=question_id)
        elif question_id == 5:
            if answer == "YOUR ANSWER HERE":
                score += 1
                return render_template(
                    'success.html',
                    score=score,
                    finished=True)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="YOUR CORRECT ANSWERE HERE",
                    finished=True)

        #TODO
        # Add 3more for each question id and fix your template accordingly
    except ValueError:
        print 'Oops thats an error should be caught'

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))