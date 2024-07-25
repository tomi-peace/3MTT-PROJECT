import spacy
from nltk.tokenize import word_tokenize
import time
text = "This is a sample text for tokenization using Spacy and NLTK."
nlp = spacy.load ("en_core_web_sm")
start_time_spacy = time.time()
doc = nlp(text)
spacy_tokens = (token.text for token in doc)
end_time_spacy = time.time()
print ("Spacy Tokens:",spacy_tokens)
print ("Time taken by Spacy:", end_time_spacy -start_time_spacy, "seconds" )
start_time_nltk = time.time ()
nltk_tokens = word_tokenize(text)
end_time_nltk = time.time ()
print ("NLTK Tokens :" , nltk_tokens)
print ("Time taken by NLTK:" ,end_time_nltk - start_time_nltk, "seconds")
