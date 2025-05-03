import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template, request, redirect, url_for

nltk.download('vader_lexicon')
app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
#get -> Sends data in the URL (e.g., ?name=John) Used for retrieving data
#post -> Sends data in the body of the request
def analyze():
    if request.method == "POST":
        user_statements_get = (request.form['user_statements']).strip().split(',')
        positive_to_negative = sorted(
            user_statements_get , #object to be sorted
            key=lambda x: sia.polarity_scores(x)['compound'], #method of sorting criteria
            reverse=False
            )
        return render_template('analyze.html', sorted_statements=positive_to_negative)
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)