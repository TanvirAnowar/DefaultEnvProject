# Tokenization 
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer

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

ps = PorterStemmer()


#for word in doc_corpus:
 #   print(word + ' --> ' + ps.stem(word))
    
    
reg = RegexpStemmer('ing$|s$|ed$|able$', min=4)
#for word in doc_corpus:
 #   print(word + ' --> ' + reg.stem(word))
    
#snowball stammer

sb = SnowballStemmer('english')

for word in doc_corpus:
    print(word + ' --> ' + sb.stem(word))