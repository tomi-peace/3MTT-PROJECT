import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
text = "NLTK is a powerful tool for natural language processing."
tokens = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
lemmatized_words = (lemmatizer.lemmatize(word) for word in tokens)
print("Lemmatized words:", lemmatized_words)
stemmer =PorterStemmer()
stemmed_words = (stemmer.stem(word) for word in tokens)
print ("Stemmed words:", stemmed_words)