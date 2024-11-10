from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# API URL for random advice
API_URL = "https://api.adviceslip.com/advice"  # External API for random advice

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/get_response', methods=['POST'])
def get_response():
    user_question = request.json.get('question')  # Get the user's question from the request
    
    # Make a request to the external API to get random advice
    try:
        response = requests.get(API_URL)  # Send GET request to fetch random advice
        response_data = response.json()  # Convert the API response to JSON
        bot_response = response_data.get('slip', {}).get('advice', 'No advice found')  # Extract advice from the response
    except Exception as e:
        bot_response = f"Error fetching response from API: {str(e)}"
    
    return jsonify({'response': bot_response})  # Send the response from the API

if __name__ == '__main__':
    app.run(debug=True)
