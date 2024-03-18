from flask import Flask, render_template, request, jsonify
from g4f.client import Client
import re

app = Flask(__name__)
client = Client()

@app.route('/')
def home():
    return render_template('index.html')

def extract_three_sentences(text):
    # Use regular expression to split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return '. '.join(sentences[:3])

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}],
    )
    bot_response = response.choices[0].message.content
    bot_response_first_three_sentences = extract_three_sentences(bot_response)
    return jsonify({'bot_response': bot_response_first_three_sentences})

# if __name__ == '__main__':
#     app.run(debug=True)
