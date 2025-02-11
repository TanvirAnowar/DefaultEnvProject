# Tokenization 
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer
# Download the necessary NLTK data
nltk.download('punkt_tab')
nltk.download('punkt')

corpus = '''hello welcome to the world of programming. we are learning python programming, please stay with us! put's man.so are you ready to learn python programming? lets start!'''

documents = sent_tokenize(corpus)

doc = word_tokenize(documents[0])
doc_corpus = word_tokenize(corpus)

punc_tokenizer = wordpunct_tokenize(corpus)

tree_bank_tokenizer = TreebankWordTokenizer()

tree_token = tree_bank_tokenizer.tokenize(corpus)
#print(documents)

