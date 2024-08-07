import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyser 
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sid = SIA()
text = "I love this product! It's amazing."
scores = sid.polarity_scores(text)
print(scores)
if scores['compound'] >= 0.05: print("Positive sentiment")
elif scores['compound'] <= -0.05: print("Negative sentiment")
else: print("Neutral sentiment")