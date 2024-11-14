import spacy
from transformers import pipeline

# Charger le modèle spaCy pour l'analyse syntaxique
nlp = spacy.load("hba.html")

# Charger le modèle de Transformers pour l'analyse de sentiments
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Fonction pour analyser le texte et répondre
def analyze_and_respond(text):
    # Analyse syntaxique avec spaCy
    doc = nlp(text)
    print("Analyse syntaxique:")
    for token in doc:
        print(f"{token.text} ({token.pos_}) - dépendance : {token.dep_}")

    # Analyse du sentiment avec Transformers
    sentiment = sentiment_analyzer(text)[0]
    print("\nAnalyse de sentiment:")
    print(f"Sentiment : {sentiment['label']} avec une confiance de {sentiment['score']:.2f}")

    # Réponse en fonction du sentiment
    if sentiment["label"] == "POSITIVE":
        response = "Je suis heureux d'entendre cela ! 😊"
    else:
        response = "Oh, ça n'a pas l'air d'aller très bien... 😟 Je suis là si vous avez besoin de parler."
    
    return response

