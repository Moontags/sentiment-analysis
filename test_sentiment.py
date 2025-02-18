import unittest
from app import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        self.assertEqual(analyze_sentiment("This is amazing!"), "Positive")

    def test_negative_sentiment(self):
        self.assertEqual(analyze_sentiment("This is terrible!"), "Negative")

    def test_neutral_sentiment(self):
        self.assertEqual(analyze_sentiment("This is a statement."), "Neutral")

if __name__ == '__main__':
    unittest.main()
