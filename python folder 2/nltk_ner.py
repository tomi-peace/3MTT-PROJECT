import nltk
from nltk.tokenize import word_tokenize
text = "Apple Inc. was founded by Steve Jobs and Steve Wozniak in 1976. It's headquarters is located in Cupertino, California."
tokens = word_tokenize(text)
ner_tags = nltk.ne_chunk(nltk.pos_tag(tokens))
print("Named Entity Recognition (NER) Tags:")
print(ner_tags)
