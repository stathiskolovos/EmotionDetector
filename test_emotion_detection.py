"""
Statement 	Dominant Emotion
I am glad this happened 	joy
I am really mad about this 	anger
I feel disgusted just hearing about this 	disgust
I am so sad about this 	sadness
I am really afraid that this will happen 	fear

"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):
    def test_emotion_detector(self):
        test1 = emotion_detector('I am glad this happened')
        self.assertEqual(test1['dominant_emotion'], 'joy')
        test2 = emotion_detector('I am really mad about this')
        self.assertEqual(test2['dominant_emotion'], 'anger')
        test3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test3['dominant_emotion'], 'disgust')
        test4 = emotion_detector('I am so sad about this')
        self.assertEqual(test4['dominant_emotion'], 'sadness')
        test5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test5['dominant_emotion'], 'fear')

unittest.main()
