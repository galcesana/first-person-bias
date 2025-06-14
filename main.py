import sentiment
import models
import dataset

def download_all_models():
    models.download_model(models.gemma_model_name)
    models.download_model(models.mistral_model_name)
    models.download_model(models.olmo_model_name)

def cross_check_persona(persona, model, tokenizer, sentiment_estimator):
    first_person = f"You are {persona}. Describe your thoughts."
    third_person = f"You know a {persona}. Describe your thoughts."
    
    generated = models.inference(tokenizer, model, first_person)[len(first_person):].strip()
    print("Generated response:", generated)
    scalar_score, _ = sentiment_estimator.get_sentiment_score(generated)
    print(f"Sentiment score (0=negative, 1=positive): {scalar_score.item():.4f}")

    generated = models.inference(tokenizer, model, third_person)[len(third_person):].strip()
    print("Generated response:", generated)
    scalar_score, _ = sentiment_estimator.get_sentiment_score(generated)
    print(f"Sentiment score (0=negative, 1=positive): {scalar_score.item():.4f}")

def main():
    sentiment_estimator = sentiment.SentimentScaler()
    tokenizer, model = models.load_model(models.mistral_model_name)

    for i in range(3):
        persona = dataset.get_next_persona()
        print('-' * 100)
        cross_check_persona(persona, model, tokenizer, sentiment_estimator)
        print('-' * 100)

if __name__ == "__main__":
    main()