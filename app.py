from flask import Flask, request, jsonify, render_template
import requests,re

app = Flask(__name__)

# API URL for random advice
API_URL = "http://localhost:8080/api/home/random"  # External API for random advice

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/get_response', methods=['POST'])
def get_response():
    user_question = request.json.get('question')
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            bot_response = response.text
        else:
            bot_response = f"Error: Unable to fetch response from the API. Status code: {response.status_code}"
    except Exception as e:
        bot_response = f"Error fetching response from API: {str(e)}"

    # Apply bold formatting using regular expressions
    formatted_response = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', bot_response)

    return jsonify({'response': formatted_response})


if __name__ == '__main__':
    app.run(debug=True)
