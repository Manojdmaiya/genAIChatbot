# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Predefined set of bot responses
# responses = {
#     "hello": "Hi there! How can I help you?",
#     "how are you": "I'm doing great, thanks for asking!",
#     "bye": "Goodbye! Have a great day!",
# }

# @app.route('/')
# def home():
#     return render_template('index.html', title="Home", chat_history=[])

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     user_message = request.form['user_message']
#     bot_response = get_bot_response(user_message)
#     return render_template('index.html', title="Chat", chat_history=[(user_message, bot_response)])

# @app.route('/trending_questions')
# def trending_questions():
#     # Example of trending questions, can be dynamic or fetched from a database
#     trending = [
#         "What is AI?",
#         "How does Python work?",
#         "What are the latest tech trends?",
#     ]
#     return render_template('trending_questions.html', title="Trending Questions", trending=trending)

# def get_bot_response(user_message):
#     user_message = user_message.lower()
#     return responses.get(user_message, "Sorry, I didn't understand that.")

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Predefined list of random responses
random_responses = [
    "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
    "I am not sure about that, let me think...",
    "Can you clarify that a bit?",
    "I think the answer is beyond my knowledge!",
    "Let me get back to you on that!",
    "I don't know, but that's a great query!",
    "Have you checked other sources for more information?"
]

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file



@app.route('/get_response', methods=['POST'])
def get_response():
    user_question = request.json.get('question')  # Get the user's question from the request
    # Select a random response from the predefined list
    random_response = random.choice(random_responses)
    return jsonify({'response': random_response})  # Send the random response as JSON

if __name__ == '__main__':
    app.run(debug=True)
