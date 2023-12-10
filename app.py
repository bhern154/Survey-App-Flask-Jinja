from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey

responses = []

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def start_survey():
    """Shows the user the title of the survey, the instructions, and a button to start the survey"""
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    questions = satisfaction_survey.questions
    
    return render_template("survey_intro.html", title=title, instructions=instructions, questions=questions)

@app.route('/questions/<int:question>')
def survey_question(question):
    if question != len(responses):
        flash(f"Invalid question - please proceed with the survey :)")
        return redirect(f"/questions/{len(responses)}")
    else:
        question_text = satisfaction_survey.questions[question].question
        choices = satisfaction_survey.questions[question].choices
        return render_template("questions.html", question_text=question_text, choices=choices)

@app.route('/answer')
def answer():
    responses.append(request.args["choice"])
    if len(responses) < len(satisfaction_survey.questions):
        return redirect(f"/questions/{len(responses)}")
    else:
        return redirect("/thank_you")
    
@app.route('/thank_you')
def thank_you():
    return render_template("thank_you.html")