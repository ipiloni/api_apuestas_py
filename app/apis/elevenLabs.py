import requests
from flask import jsonify

from app.config import get

def llamarALaIA():
    api_key = get('API_KEY_ELEVENLABS')

    voice_id = 'D09EpJbk4um1HKSpeTSc'

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": "Wacho, este año nos vamos a recibir de Ingenieros con este maldito TePe, ¿se dan cuenta de eso?",
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, json=data, headers=headers)

    with open("vozAgustin.mp3", "wb") as f:
        f.write(response.content)

    json = {"respuesta": "Voz generada y guardada correctamente."}

    return jsonify(json), 200