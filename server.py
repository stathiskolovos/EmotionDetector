"""
Task 6: Web deployment of the application using Flask
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def render_index():
    """
    render main page of app
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_app():
    """
    text from user -> function emotion_detector -> returns response formatted as:
    For the given statement, the system response is 'anger': 0.006274985, 
    'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. 
    The dominant emotion is joy. 
    """
    user_input = request.args.get('textToAnalyze')
    response = emotion_detector(user_input)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Modify server.py to incorporate error handling when the dominant_emotion is None.
    # In this scenario, the response should display a message Invalid text! Please try again!.
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is 'anger':"
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " 
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
