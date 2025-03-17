from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect():
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    anger = result.get("anger")
    disgust = result.get("disgust")
    fear = result.get("fear")
    joy = result.get("joy")
    sadness = result.get("sadness")
    dom_emote = result.get("dominant_emotion")
    sys_resp = f'''
        For the given statement, the system response is 'anger': {anger},
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 
        'sadness': {sadness}. The dominant emotion is 
        <strong>{dom_emote}</strong>.
    '''
    return sys_resp

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)