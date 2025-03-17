from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_dominant_emotion(self):
        emotions = {
            "joy": "I am glad this happened",
            "anger": "I am really mad about this",
            "disgust": "I feel disgusted just hearing about this",
            "sadness": "I am so sad about this",
            "fear": "I am really afraid that this will happen"
        }
        for emotion, statement in emotions.items():
            dom_emote = emotion_detector(statement).get("dominant_emotion")
            self.assertEqual(dom_emote, emotion)

if __name__ == "__main__":
    unittest.main()