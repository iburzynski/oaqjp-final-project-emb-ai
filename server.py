'''
Flask server for Emotion Analysis.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect():
    '''
    Runs emotion analysis on user submitted form string.
    '''
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    anger = result.get("anger")
    disgust = result.get("disgust")
    fear = result.get("fear")
    joy = result.get("joy")
    sadness = result.get("sadness")
    dom_emote = result.get("dominant_emotion")
    if not dom_emote:
        sys_resp = "Invalid text! Please try again!"
    else:
        sys_resp = f'''
        For the given statement, the system response is 'anger': {anger},
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 
        'sadness': {sadness}. The dominant emotion is 
        <strong>{dom_emote}</strong>.
        '''
    return sys_resp

@app.route("/")
def index():
    '''
    Renders the index page.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    