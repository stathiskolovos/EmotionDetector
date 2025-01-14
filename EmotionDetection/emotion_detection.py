import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  { "raw_document": { "text": text_to_analyse } }

    # get response
    response = requests.post(URL, json = input_json, headers = headers)
    
    # Convert the response text into a dictionary using the json library functions.
    formatted = json.loads(response.text)

    # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
    if response.status_code == 200:        
        anger_score = formatted["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted["emotionPredictions"][0]["emotion"]["sadness"]

    # Write the code logic to find the dominant emotion, which is the emotion with the highest score.
        emotions = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        dominant_emotion_index = emotions.index(max(emotions))
        emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        dominant_emotion = emotion_keys[dominant_emotion_index]

    # Access the status_code attribute of the server response to correctly display the system response for blank entries.
    # For status_code = 400, make the function return the same dictionary, but with values for all keys being None.

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # modify the emotion_detector function to return the following output format.
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result