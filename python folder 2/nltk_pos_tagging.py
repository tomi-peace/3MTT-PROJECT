import nltk
from nltk.tokenize import word_tokenize
text = "NLTK is a powerful tool for natural language processing."
tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
print("part-of-speech Tags:",pos_tags)

import nltk
nltk.download('averaged_perceptron_tagger')