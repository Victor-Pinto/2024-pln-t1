from flask import Flask, jsonify, request

from loader import model1, model2, model3, model_stemmer, model_lemmatize
from stanza_loader import stanza_model
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Permite todas las solicitudes CORS

@app.route("/ping", methods=['GET'])
def pong():
  return jsonify({"message": "pong"})


@app.route("/tokenize/<int:alg>", methods=['POST'])
def ms_tokenize(alg):
  text = request.json['text']
  result = {
    1: model1.tokenize(text),
    2: model2.tokenize(text),
    3: model3.tokenize(text),
  }[alg]
  return jsonify({"text": text, "algorithm":alg, "tokenized":result})


@app.route("/stemmer", methods=['POST'])
def ms_stemmer():
  text = request.json['text']
  result = model_stemmer.stemmer(text)
  return jsonify({"text": text, "algorithm":"SnowballStemmer", "stemmer":result})


@app.route("/lemmatize", methods=['POST'])
def ms_lemmatize():
  text=request.json['text']
  result = model_lemmatize.lemmatize(text)
  return jsonify({"text": text, "algorithm":"lemmatize", "lemma":result})

@app.route("/stanza", methods=['POST'])
def ms_stanza():
  text = request.json['text']
  result = stanza_model.stanza_process(text)
  return jsonify({"text": text, "algorithm":"stanza", "stanza":result})




if __name__ == "__main__":
  app.run(debug=True)