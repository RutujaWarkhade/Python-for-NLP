# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:40:00 2024

@author: OM
"""

###You can notice that am,is,of,the most,popular,in are missing
####################################
#suppose we want to replace words in string
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

#################################
#suppose we want auto correction in the sentence
from  autocorrect import Speller
#declare the function Speller defined for English
spell=Speller(lang="en")
spell("Rutuja")

####################################

#suppose we want to correct whole sentence
from  autocorrect import Speller
spell=Speller(lang="en")
import nltk
nltk.download("punkt")
from nltk import word_tokenize
sentence3="mararrthi is verry papular language in maharastra"
##let us first tokenize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)




#########################################
##Stemming 
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("Jumping")
stemmer.stem("Jumped")


####################################
#Lematizer
#lematizer looks into dictionary words
import nltk
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")
##############################################


##chunking (Shallow Parsing) Identifying named entites
nltk.download("maxent_ne_chunker")
nltk.download("words")
sentence4="We are learning NLP in python by SanjivaniAI"
#first we will tokenize
nltk.download('averaged_perceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]



##################################
#sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are Learning NLP in Python. Delivered by sanjivani")
sent
##['we are learning NLP in Python.','Delivered by Sanjivani']
####################################
#He went to bank and checked account it was almost 0
#looking this he went to river bank and was crying
from nltk.wsd import lesk
sentence1="keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
####output Synset('savings_bank.n,02')
sentence2="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
###Synset('bank.v.07')