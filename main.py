import openai
import matplotlib.pyplot as plt
from textblob import TextBlob
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to interact with OpenAI GPT-3 model
def gpt3_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error in generating response: {str(e)}"

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Function to generate sentiment report and pie chart visualization
def generate_report(sentiments):
    positive = sentiments.count('Positive')
    negative = sentiments.count('Negative')
    neutral = sentiments.count('Neutral')

    # Data visualization - Pie Chart
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [positive, negative, neutral]
    colors = ['lightgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0)  # explode the 1st slice (Positive)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.title("Sentiment Analysis Report")
    plt.savefig('sentiment_report.png')  # Save the figure
    plt.show()  # Display the figure

    print("\nSentiment Summary:")
    print(f"Positive: {positive}, Negative: {negative}, Neutral: {neutral}")

# Main interactive program
def main():
    print("Welcome to the GPT-3 Interactive Sentiment Analysis Program!\n")
    
    conversation = []
    sentiments = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending the conversation...")
            break

        # Generate response from GPT-3
        response = gpt3_response(user_input)
        print(f"GPT-3: {response}")
        conversation.append({"User": user_input, "GPT-3": response})

        # Analyze sentiment
        sentiment = analyze_sentiment(response)
        sentiments.append(sentiment)
        print(f"Sentiment: {sentiment}\n")
    
    # Generate sentiment report and visualizations
    generate_report(sentiments)

if __name__ == "__main__":
    main()