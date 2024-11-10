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


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('question')  # Get the question from the request
    # You can add your logic for generating a response here
    bot_response = f"Bot response to: {user_input}"  # Example response logic
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)