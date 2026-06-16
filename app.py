from flask import Flask, render_template, request

app = Flask(__name__)

def predict_segment(income, score):

    if income >= 70 and score >= 70:
        return "Premium Customer"

    elif income >= 70 and score < 40:
        return "High Income - Low Spending Customer"

    elif income < 40 and score >= 60:
        return "Budget Friendly Customer"

    else:
        return "Regular Customer"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    income = float(request.form['income'])
    score = float(request.form['score'])

    result = predict_segment(income, score)

    return render_template(
        'index.html',
        prediction=result
    )

if __name__ == "__main__":
    app.run(debug=True)
