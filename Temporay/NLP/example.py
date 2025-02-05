# Tokenization 
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download the necessary NLTK data
nltk.download('punkt')

corpus = '''hellow welcome to the world of programming, 
            we are learning python programming, please stay with us!
            so are you ready to learn python programming? lets start!'''

sent_tokenize(corpus)
