# Tokenization 
import nltk
from nltk.tokenize import sent_tokenize

# Download the necessary NLTK data
nltk.download('punkt_tab')
nltk.download('punkt')

corpus = '''hello welcome to the world of programming. we are learning python programming, please stay with us! so are you ready to learn python programming? lets start!'''

documents = sent_tokenize(corpus)

#print(documents)

