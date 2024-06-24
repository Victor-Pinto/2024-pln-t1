import joblib

class Model:
    model = None
    def __init__(self, path:str):
        self.model = self.load_model(path)
        

    def load_model(self, path:str):
        try:
            return joblib.load(path)
            
        except Exception as ee:
            print("model not found")
            return None
    
        
class TokenizeModel(Model):
    def __init__(self, path):
        super().__init__(path)

    def tokenize(self, text):
        
        if(self.model):
            return self.model.tokenize(text)
        else:
            return None, "model not found"
        
        
class StemmerModel(Model):
    def __init__(self, path, tokenize_model):
        super().__init__(path)
        self.tokenize_model = tokenize_model

    def stemmer(self, text):
        
        if(self.model):
            sent_tokenization = self.tokenize_model.tokenize(text)
            return [self.model.stem(a_token) for a_token in sent_tokenization]
            
        else:
            return None, "model not found"

import nltk
from nltk.stem import WordNetLemmatizer


class LemmatizeModel():
    def __init__(self, tokenize_model):
        self.tokenize_model = tokenize_model
        nltk.download("wordnet")
        self.model_lemm = WordNetLemmatizer()

    def lemmatize(self, text):
        
        sent_tokenization = self.tokenize_model.tokenize(text) 
        return [self.model_lemm.lemmatize(a_token) for a_token in sent_tokenization] 

model1 = TokenizeModel("models/model1.pkl")
model2 = TokenizeModel("models/model2.pkl")
model3 = TokenizeModel("models/model3.pkl")
model_stemmer = StemmerModel("models/model4.pkl", model2)
model_lemmatize = LemmatizeModel(model2)

