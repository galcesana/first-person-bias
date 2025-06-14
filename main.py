import sentiment
import models

def download_all_models():
    models.download_model(models.gemma_model_name)
    models.download_model(models.mistral_model_name)
    models.download_model(models.olmo_model_name)

def main():
    sentiment_estimator = sentiment.SentimentScaler()

    tokenizer, model = models.load_model(models.gemma_model_name)
    while True:
        user_prompt = input("Enter your prompt: ")
        generated = models.inference(tokenizer, model, user_prompt)
        print("Generated response:", generated)

        scalar_score, _ = sentiment_estimator.get_sentiment_score(generated)
        print(f"Sentiment score (0=negative, 1=positive): {scalar_score.item():.4f}")

if __name__ == "__main__":
    main()