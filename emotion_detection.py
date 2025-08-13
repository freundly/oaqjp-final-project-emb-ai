import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {"text": text_to_analyze}
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        
        # Watson cevabını dict olarak alıyoruz
        emotions = result.get("emotion", {})  # emotion objesi
        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)
        
        # Dominant duyguyu bul
        dominant_emotion = max(
            {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness},
            key=lambda k: {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness}[k]
        )
        
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": f"{response.status_code}: {response.text}"}
