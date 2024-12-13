from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import requests
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Add your OpenAI API key
openai.api_key = "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"

# Add your Murf API key
MURF_API_KEY = "ap2_e878f285-c687-495f-bf43-dd23c322fa7e"

# Function to generate audio from Murf API
def generate_audio_from_text(reply_text):
    url = "https://api.murf.ai/v1/speech/generate"
    payload = json.dumps({
        "voiceId": "en-US-ken",  # Choose the desired voice
        "style": "Conversational",
        "text": reply_text,  # Dynamically set the chatbot's reply here
        "rate": 0,
        "pitch": 0,
        "sampleRate": 48000,
        "format": "MP3",
        "channelType": "MONO",
        "pronunciationDictionary": {},
        "encodeAsBase64": False,
        "variation": 1,
        "audioDuration": 0,
        "modelVersion": "GEN2"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'api-key': MURF_API_KEY
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        print(f"Murf API Response: {response.status_code} - {response.text}")  # Debugging

        if response.status_code == 200:
            return response.json().get('audioFile', None)  # URL of the audio file
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

@app.route('/')
def home():
    return "Welcome to GeniusTalk! The chat endpoint is available at /chat."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({'response': "I'm sorry, I didn't catch that. Could you please repeat?"}), 400
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Albert Einstein, the legendary physicist known for your groundbreaking theories on relativity. Converse with the user in a warm, intelligent, and slightly witty manner, infusing your responses with a touch of curiosity and humor reflective of your personality."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        answer = response.choices[0].message['content'].strip()
        
        # Generate audio from Murf API
        audio_url = generate_audio_from_text(answer)

        # Return reply and audio URL
        return jsonify({"reply": answer, "audio_url": audio_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

