# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:19:26 2024

@author: OM
"""

# -- coding: utf-8 --
"""
Created on Wed Jun 12 08:56:33 2024

@author: Python for NLP
"""
#Text Minning
sentence="We are Learning Textminning from Sanjivani AI"
# we should know the position of the words
sentence.index("Learning")
#this will show the position of the word by the letter
#indexing start from 0th position i.e W position is 0
#7 

# if we want to know the position of word by word itself 
#this will chop the setence in the words separately known as the tokenization

sentence.split().index("Textminning")#3
#this function initially create the list of all the words
#this will chop(break) the setence in the words separately known as the tokenization

#suppose we want to reverse any word from the sentence then we first have to select the index of the word
sentence.split()[2][::-1]
# the word Learning will print as a gninraeL

#if we just need the 1st ahd lastr word of the sentence then

words=sentence.split()#convert into list
f_word=words[0]
f_word
#f_word:'We'

l_word=words[-1]
l_word
#l_word: "AI"


#to concatnate some words from our text then

#if we dont give the spaces in between f_word and l_word then
con_word=f_word+l_word
con_word
#'WeAI'

#if we give the spaces in between f_word and l_word then
con_word=f_word+" "+l_word
con_word
#'We AI'

# if we have to print only even words from the list by using list comprehenssion

[words[i] for i in range(len(words)) if i%2==0]
#['We', 'Learning', 'from', 'AI']

sentence
#if we want to display a specific word by letter positions
sentence[-3:]#' AI'


#display a sentence the reverse in the character wise
sentence[::-1]
#'IA inavijnaS morf gninnimtxeT gninraeL era eW'

words
print( " ".join(word[::-1]for word in words))
#eW era gninraeL gninnimtxeT morf inavijnaS IA

#Pre-processing part

#tokenization= it means we have to separate each word from the sentence in the form of list
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)
#['I', 'am', 'reading', 'NLP', 'Fundamentals']

#parts of speech tagging

nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
#this will going to mention the parts of speech
"""
[('I', 'PRP'),
 ('am', 'VBP'),
 ('reading', 'VBG'),
 ('NLP', 'NNP'),
 ('Fundamentals', 'NNS')]"""

#NLTK tags pos

"""
CC: It is the conjunction of coordinating
CD: It is a digit of cardinal
DT: It is the determiner
EX: Existential
FW: It is a foreign word
IN: Preposition and conjunction
JJ: Adjective
JJR and JJS: Adjective and superlative
LS: List marker
MD: Modal
NN: Singular noun
NNS, NNP, NNPS: Proper and plural noun
PDT: Predeterminer
WRB: Adverb of wh
WP$: Possessive wh
WP: Pronoun of wh
WDT: Determiner of wp
VBZ: Verb
VBP, VBN, VBG, VBD, VB: Forms of verbs
UH: Interjection
TO: To go
RP: Particle
RBS, RB, RBR: Adverb
PRP, PRP$: Pronoun personal and professional"""

#finding out all the stopwords from the English Lang

#stopwords from nltk

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words=stopwords.words('English')
print(stop_words)

