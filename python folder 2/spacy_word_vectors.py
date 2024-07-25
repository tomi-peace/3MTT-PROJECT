import spacy
text = "banana apple orange"
nlp = spacy.load ("en_core_web_sm")
doc = nlp (text)
print (token.text, token.vector)