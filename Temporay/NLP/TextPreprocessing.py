import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download the necessary NLTK data
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_english')

lemma = WordNetLemmatizer()

#corpus = '''hello welcome to the world of programming. we are learning python programming, please stay with us! put's man.so are you ready to learn python programming? lets start!'''

#doc_corpus = word_tokenize(corpus)

#? Lemmatization

# for word in doc_corpus:
#     print(word + ' --> ' + lemma.lemmatize(word, pos='v'))
    
    
#print(lemma.lemmatize('programming', pos='v'))

#Stops words

sentance = '''
I have a dream that one day down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification – one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers.

I have a dream today.

I have a dream that one day every valley shall be exalted, and every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed and all flesh shall see it together.

This is our hope. This is the faith that I go back to the South with. With this faith we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day.

This will be the day, this will be the day when all of God’s children will be able to sing with new meaning “My country ’tis of thee, sweet land of liberty, of thee I sing. Land where my father’s died, land of the Pilgrim’s pride, from every mountainside, let freedom ring!
'''

#? 1. Tokenize the sentance
sentence_token = sent_tokenize(sentance)
# print(type(sentence_token))

#? 2. Tokenize the words
sentences_after_join = []

ps = PorterStemmer()
sbs = SnowballStemmer('english')
wnlem = WordNetLemmatizer()
for i in range (len(sentence_token)):
    word_token = word_tokenize(sentence_token[i])
    
    #? 3. Remove the stop words
    words = [word for word in word_token 
            if word.lower() not in stopwords.words('english')]
    pos_tag = nltk.pos_tag(words)
    
    word_token_after_steaming = [ps.stem(word) for word in word_token 
                                 if word.lower() not in stopwords.words('english')]
    
    word_token_after_steaming_snowball = [sbs.stem(word) for word in word_token 
                                  if word.lower() not in stopwords.words('english')]
    
    word_token_after_lemmeatizer = [wnlem.lemmatize(word, pos='v') for word in word_token 
                                  if word.lower() not in stopwords.words('english')]
    
    # sentences_after_join.append(' '.join(word_token_after_steaming))
    
    # sentence_token[i]   = ' '.join(word_token_after_lemmeatizer)
    
print(pos_tag)
# print(word_token_after_steaming)
# print(word_token_after_steaming_snowball)
    
    







