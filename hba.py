from flask import Flask, render_template, request, jsonify
import spacy
from transformers import pipeline

# Initialiser Flask
app = Flask(__name__)

# Charger le modèle spaCy pour l'analyse syntaxique
nlp = spacy.load("en_core_web_sm")  # Remplacez par le modèle que vous voulez utiliser

# Charger le modèle de Transformers pour l'analyse de sentiments
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Route principale
@app.route('/')
def index():
    return render_template('index.html')

# Route pour l'analyse du texte
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']

    # Analyse syntaxique avec spaCy
    doc = nlp(text)
    syntax_analysis = [{'text': token.text, 'pos': token.pos_, 'dep': token.dep_} for token in doc]

    # Analyse du sentiment avec Transformers
    sentiment = sentiment_analyzer(text)[0]
    response = {
        'syntax': syntax_analysis,
        'sentiment': sentiment['label'],
        'confidence': sentiment['score']
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


