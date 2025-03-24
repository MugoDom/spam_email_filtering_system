# test.py
import unittest
from predict import predict

class TestLogisticRegression(unittest.TestCase):
    def test_spam(self):
        self.assertEqual(predict("Free entry in 2 a wkly comp to win FA Cup final"), 1)
    
    def test_ham(self):
        self.assertEqual(predict("Hey, how are you doing today?"), 0)

if __name__ == "__main__":
    unittest.main()