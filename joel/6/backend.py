from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('quiz.html')

@app.route('/quiz-submit', methods=['POST'])
def quiz_submit():
    # Get form data
    question1 = request.form['question1']
    question2 = request.form['question2']

    # Perform quiz validation
    if question1.lower() == 'paris' and question2.lower() == 'leonardo da vinci':
        result = 'Congratulations! You answered all the questions correctly.'
    else:
        result = 'Sorry, your answers are incorrect. Please try again.'

    return render_template('quiz-result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
