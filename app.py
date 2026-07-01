from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# load trained model
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    # get input values
    income = float(request.form['income'])
    loanamount = float(request.form['loanamount'])
    credithistory = float(request.form['credithistory'])

    # ML prediction
    prediction = model.predict([[income, loanamount, credithistory]])

    # result logic
    if prediction[0] == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    return f"""
    <html>
        <body style="text-align:center; margin-top:100px; font-family:Arial;">
            <h1>{result}</h1>
            <a href="/">Go Back</a>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)