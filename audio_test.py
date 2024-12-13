import requests
import json

url = "https://api.murf.ai/v1/speech/generate"
payload = json.dumps({
    "voiceId": "en-US-ken",
    "style": "Conversational",
    "text": "Relativity is a fascinating concept!",
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
    "Content-Type": "application/json",
    "Accept": "application/json",
    "api-key": "ap2_e878f285-c687-495f-bf43-dd23c322fa7e"  # Replace with your API key
}

response = requests.post(url, headers=headers, data=payload)
print(response.status_code)
print(response.text)
