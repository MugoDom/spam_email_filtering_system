# Predict.py
import joblib

def predict(message):
    model = joblib.load('../../models/linear_regression.pkl') 
    vectorizer = joblib.load('../../models/tfidf_vectorizer.pkl')
    
    message_tfidf = vectorizer.transform([message])
    return model.predict(message_tfidf)[0]

if __name__ == "__main__":
    print(predict("Free money now! Click here!"))