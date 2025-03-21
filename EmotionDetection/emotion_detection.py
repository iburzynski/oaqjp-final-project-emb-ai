import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Performs emotion analysis on a string with the Watson NLP API.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    resp = requests.post(url=url, headers=header, json=my_obj)
    if resp.status_code == 400:
        emotions = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        resp_json = json.loads(resp.text)
        emotions = resp_json.get("emotionPredictions")[0].get("emotion")
        max_score = 0
        dominant_emotion = None
        for emotion, score in emotions.items():
            if score > max_score:
                max_score = score
                dominant_emotion = emotion
        emotions["dominant_emotion"] = dominant_emotion
    return emotions