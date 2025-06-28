import sentiment
import models
import dataset
import csv

def download_all_models():
    models.download_model(models.gemma_model_name)
    models.download_model(models.mistral_model_name)
    models.download_model(models.qwen_model_name)

def cross_check_persona(persona, model, tokenizer, sentiment_estimator):
    results = []
    questions = dataset.get_persona_questions(persona)
    for key, question_list in questions.items():
        for q in question_list[:5]:
            print(f"Question ({key}): {q}")
            generated = models.inference(tokenizer, model, q)[len(q):].strip()
            print("Generated response:", generated)
            scalar_score, _ = sentiment_estimator.get_sentiment_score(generated)
            print(f"Sentiment score (0=negative, 1=positive): {scalar_score.item():.4f}")
            results.append(generated)
            results.append(scalar_score.item())
        for q in question_list[5:]:
            print(f"Question ({key}): {q}")
            generated = models.inference(tokenizer, model, q)[len(q):].strip()
            print("Generated response:", generated)
            results.append(generated)
    return results

def main():
    sentiment_estimator = sentiment.SentimentScaler()
    tokenizer, model = models.load_model(models.mistral_model_name)

    with open('mistral_result.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        headers = ['sex', 'age', 'occupation', 'country', 'marital_status']
        first_headers = []
        third_headers = []
        for i in range(1, 6):
            first_headers += [f'first_q{i}', f'first_score{i}']
            third_headers += [f'third_q{i}', f'third_score{i}']
        for i in range(6,11):
            first_headers += [f'first_q{i}']
            third_headers += [f'third_q{i}']
        headers += first_headers + third_headers
        writer.writerow(headers)

        while (persona := dataset.get_next_persona()) != None:
            print('-' * 100)
            result = cross_check_persona(persona, model, tokenizer, sentiment_estimator)
            print('-' * 100)
            writer.writerow(result)

if __name__ == "__main__":
    main()