from textblob import TextBlob
import pandas as pd

data = {
    "Text": [
        "I love this product, it's amazing!",
        "This is the worst experience ever.",
        "The product is okay, not bad.",
        "Absolutely fantastic service!",
        "I am very disappointed with the quality.",
        "It works fine, nothing special."
    ]
}

df = pd.DataFrame(data)

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Text"].apply(get_sentiment)

print(df)
print("\nSentiment Count:")
print(df["Sentiment"].value_counts())
