# GPT-3 Interactive Sentiment Analysis Program

Welcome to the GPT-3 Interactive Sentiment Analysis Program! 
This program utilizes OpenAI's GPT-3.5-turbo model to generate responses based on user input, performs sentiment analysis on the generated text, and provides a user-friendly interactive experience.

## Features

- Interactive User Interface: Engage in a conversation with the AI model.
- Response Generation: Generate coherent responses using OpenAI's GPT-3.5-turbo model.
- Sentiment Analysis: Analyze the sentiment of the generated responses (e.g., positive, neutral, negative).
- Data Visualization: Generate visual reports summarizing sentiment analysis results.

## Prerequisites

Before running the program, ensure you have the following:

- Python 3.7 or later
- An OpenAI API key (you can get one by signing up at [OpenAI](https://platform.openai.com/))

## Installation

1. Clone the Repository:
```bash
  git clone https://github.com/yourusername/gpt3-sentiment-analysis.git
  cd gpt3-sentiment-analysis
```

2. Create a Virtual Environment (Optional but Recommended):
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the Required Packages:
```bash
  pip install -r requirements.txt
```
4. Set Up Environment Variables:

   Create a file named .env in the root directory of the project and add your OpenAI API key:
```bash
  OPENAI_API_KEY=your_openai_api_key_here
```

## Usage
To run the program, execute the following command:
```bash
python main.py
```

## Interacting with the Program
The program will prompt you to enter text.

Type your input and press Enter.

The GPT-3 model will respond based on your input, followed by a sentiment analysis result.

## Example Interaction:

Welcome to the GPT-3 Interactive Sentiment Analysis Program!

You: hi
GPT-3: I'm just a virtual assistant, but I'm here to help! How can I assist you today?

Sentiment: Neutral

To exit the conversation, type exit.

## Report and Visualization
After completing the conversation, a pie chart named sentiment_report.png will be generated, showing the percentage of positive, negative, and neutral sentiments.

## Acknowledgments
OpenAI for providing the GPT-3 model.

Hugging Face for their contributions to NLP.

The community for their continuous support and feedback.

## Contact Details
Name - Shatakshi Chandra

Ph. number - (+91)9149177279

mail - shatakshi0420@gmail.com
