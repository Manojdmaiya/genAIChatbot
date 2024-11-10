from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# API URL for random advice
API_URL = "http://localhost:8080/api/home/random"  # External API for random advice

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file
@app.route('/get_response', methods=['POST'])
def get_response():
    user_question = request.json.get('question')  # Get the user's question from the request
    
    # Make a request to the external Java API to get random advice
    try:
        response = requests.get(API_URL)  # Send GET request to fetch random advice
        if response.status_code == 200:
            bot_response = response.text  # Extract the string response from the API
        else:
            bot_response = f"Error: Unable to fetch response from the API. Status code: {response.status_code}"
    except Exception as e:
        bot_response = f"Error fetching response from API: {str(e)}"
    
    return jsonify({'response': bot_response})  # Send the response from the API

if __name__ == '__main__':
    app.run(debug=True)
