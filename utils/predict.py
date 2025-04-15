from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def get_sentiment(message):
    result = classifier(message)[0]
    label = result['label']
    
    if label == 'POSITIVE':
        return "😊 You seem positive. Keep it up!"
    elif label == 'NEGATIVE':
        return "😟 I'm sensing stress. Let's talk or try some calming activities."
    else:
        return "🤔 Not sure how you're feeling. Want to tell me more?"
