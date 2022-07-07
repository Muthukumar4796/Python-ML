import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk import word_tokenize
import re


str = "Adolf Hitler was born on April 20, 1889, in Braunau am Inn, a small Austrian town near the Austro-German frontier. " \
      "After his father, Alois, retired as a state customs official, " \
      "young Adolf spent most of his childhood in Linz, the capital of Upper Austria."
# print(word_tokenize(str))
result = re.sub(r"[,@/'?\.$%_()-]", "", str)
# print(result)

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
words = word_tokenize(str)
# print(words)
stemmed_words = [stemmer.stem(word) for word in words]
# print(stemmed_words)

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = word_tokenize(str)
print(words)

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)

