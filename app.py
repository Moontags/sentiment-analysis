from flask import Flask, render_template, request # type: ignore
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os


nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Analyzes the sentiment of given text and returns the result."""
    sentiment_score = sia.polarity_scores(text)['compound']
    
    if sentiment_score > 0.05:
        return "Positive"
    elif sentiment_score < -0.05:
        return "Negative"
    else:
        return "Neutral"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)