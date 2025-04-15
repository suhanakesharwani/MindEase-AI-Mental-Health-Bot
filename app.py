from flask import Flask, render_template, request
from utils.predict import get_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = get_sentiment(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
