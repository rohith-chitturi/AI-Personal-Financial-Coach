import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class ExpenseCategorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
        self.is_trained = False
        
    def train_placeholder(self):
        # Placeholder training data
        texts = ["uber ride", "walmart groceries", "netflix subscription", "salary deposit"]
        labels = ["transportation", "groceries", "entertainment", "income"]
        
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)
        self.is_trained = True
        
    def predict(self, text: str):
        if not self.is_trained:
            self.train_placeholder()
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]

categorizer = ExpenseCategorizer()
