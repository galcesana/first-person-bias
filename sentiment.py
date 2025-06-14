import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

# Sentiment label mapping
LABELS_ORDERED = ['negative', 'neutral', 'positive']

class SentimentScaler(object):
    def __init__(self):
        self.load_model()

    def get_sentiment_score(self, sentence):
        def convert_to_scalar_score(scores):
            # weighted sum to 0.5 being neutral, 1 is positive, 0 negative
            return 0.5 + ((scores[2] - scores[0]) / 2)

        # Tokenize input
        inputs = self.tokenizer(sentence, return_tensors="pt").to(DEVICE)

        # Forward pass
        with torch.no_grad():
            outputs = self.model(**inputs)
            scores = F.softmax(outputs.logits, dim=1).squeeze()

        # Convert to scalar sentiment score in [0, 1]
        score = convert_to_scalar_score(scores)
        return score, scores
    
    def load_model(self):
        model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name,
                                                                        device_map=DEVICE)  

# Example
def main():
    model = SentimentScaler()

    while True:
        # Text to analyze
        text = input("Enter text to analyze sentiment (or 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        
        # Get sentiment scores
        scalar_score, sentence_score = model.get_sentiment_score(text)

        # Print details
        for label, s in zip(LABELS_ORDERED, sentence_score):
            print(f"{label}: {s.item():.4f}")
        print(f"\nSentiment score (0=negative, 1=positive): {scalar_score.item():.4f}")


if __name__ == "__main__":
    main()