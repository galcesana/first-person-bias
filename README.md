# Persona-based Sentiment Analysis with LLMs

This project analyzes how different large language models (LLMs) respond to questions when adopting various personas, and measures the sentiment of their responses.

## Features

- **Persona Generation:** Creates diverse personas by mixing attributes like sex, age, occupation, country, and marital status.
- **Question Generation:** Retrieves or generates questions tailored to each persona.
- **Model Inference:** Uses Together AI API to query multiple LLMs (Mistral, Gemma, Qwen) for answers.
- **Sentiment Analysis:** Evaluates the sentiment of each generated response.
- **Results Logging:** Stores all results in CSV files for further analysis.

## Setup

1. **Clone the repository** and install dependencies:
    ```sh
    pip install requests
    ```

2. **Set your Together AI API key** as an environment variable:

    - On Windows (Command Prompt):
      ```
      set TOGETHER_API_KEY=your-key-here
      ```
    - On macOS/Linux:
      ```
      export TOGETHER_API_KEY=your-key-here
      ```

3. **Run the main script:**
    ```sh
    python main.py
    ```

## File Structure

- `main.py` — Main script for running the experiments.
- `generate_personas` — Script for generating persona combinations.
- `dataset.py` — Module for persona-specific question generation.
- `sentiment.py` — Module for sentiment analysis.
- `personas.csv` — Generated personas.
- `<model_name>_result.csv` — Results for each model.

## How It Works

1. **Personas** are generated and stored in a CSV file.
2. For each persona, a set of questions is retrieved.
3. Each question is sent to the selected LLM via the Together AI API.
4. The response is analyzed for sentiment.
5. All data is saved for later analysis.

## Notes

- The script automatically handles rate limiting (429 errors) by retrying after a short delay.
- Results for each model are saved in separate CSV files (e.g., `mistral_result.csv`).

## Citation

If you use this project, please cite relevant LLM and sentiment analysis papers/tools.

## License

MIT License
