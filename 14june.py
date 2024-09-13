# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:11:31 2024

@author: OM
"""

'''
Removing special characters

special character, as you know, are non-alphanumeric
These character are most often found in comments,
reference, currency numbers etc. These characters add no
value to text-understanding and induce noise into 
algorithms for that regex package is used
'''

"""

r'@\w+'
@: Matches the @ symbol.
\w+: Matches one or more word characters following the @.


"""
import re
chat1="Hello, I am having an issue with my order # 412889912"
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern, chat1)
matches




"""
The square brackets [^\d]* ensure that 
any non-digit characters between "order" 
and the digits are included in the match, 
while the parentheses (\d*) specifically capture 
the digits for extraction.

"""
##################################
import re
chat2="I have a problem with my order number 41889912"
pattern="order[^\d]*(\d*)"
matches=re.findall(pattern, chat2)
matches
###################################
chat3="My order 412889912 is having an issue, I was charged"
#pattern='order (\d*)'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern, chat3)
matches
######################################

def get_pattern_match(pattern, text):
    matches=re.findall(pattern, text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d)',chat1)
########################################

"""
18 JUNE
"""

chat1="you ask lot of questions 1235678912, abc@xyz.com"
chat2="here it is: (123)-567-8912, abc@xyz.com"
chat3="yes, phone: 1235678912 email: abc@xyz.com"
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
#######################################
#back slash (\) it is use to get symbol like((,\.{) to get as it is
#d{10} it means all 10 digit number
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)

########################################
import re
text="""
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
"""
def get_pattern_match(pattern, text):
    matches=re.findall(pattern, text)
    if matches:
        return matches[0]
get_pattern_match(r'age (\d+)',text)
#'52'

"""
age : This matches the literal text "age " in the input text.

(\d+): This is a capturing group.

\d+: This matches one or more digits.
The parentheses () around \d+ create a capturing group that extracts and returns the matched digits.

"""
#get_pattern_match(r'age (\d{2})',text)
#'52'
#get_pattern_match(r'age \d{2}',text)
#'age 52'


get_pattern_match(r'age \d+',text)
#age 52
get_pattern_match(r'Born(.*)\n',text).strip()
#r means follw regex * means select all 
#. means select 1 character before 
#hence here (.*)\n select one character i.e space 
#before all text until \n i.e new line
#after that use strip() function to remove space in o/p
#'Elon Reeve Musk'



get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
#'June 28, 1971'



get_pattern_match(r'\(age.*\n(.*)',text)
#'Pretoria, Transvaal, South Africa'
######################################################

#19 JUNE
#whether your function return multiple varible and how(interview question)
import re
text="""
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
"""
def get_pattern_match(pattern, text):
    matches=re.findall(pattern, text)
    if matches:
        return matches[0]
def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)
"""
output:
{'age': 52,
 'name': 'Elon Reeve Musk',
 'birth_date': 'June 28, 1971',
 'birth_place': 'Pretoria, Transvaal, South Africa'}
"""
def extracted_text(text):
    age=get_pattern_match('age (\d{2})',text)
    age1=get_pattern_match('age \d{2}',text)
    date=get_pattern_match('Born(.*)\n',text).strip()
    a=get_pattern_match('Born.*\n(.*)\(',text).strip()
    b=get_pattern_match('Parents.*\n(.*)',text)
    return{
    'age':int(age),
    'age1':age1,
    'date':date,
    'a':a,
    'b':b
            }
extracted_text(text)
"""
Out[72]: 
{'age': 67,
 'age1': 'age 67',
 'date': 'Mukesh Dhirubhai Ambani',
 'a': '19 April 1957',
 'b': 'Dhirubhai Ambani (father)'}

"""






#do same text for mukesh ambani
text="""
Born	Mukesh Dhirubhai Ambani
    19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
"""
"""
output:
{'age': 67,
 'name': 'Mukesh Dhirubhai Ambani',
 'birth_date': '19 April 1957',
 'birth_place': 'Aden, Colony of Aden'}
"""


def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('age (\d{2})',text)
#'67'
get_pattern_match('age \d{2}',text)
#age '67'
get_pattern_match('Born(.*)\n',text).strip()
#'Mukesh Dhirubhai Ambani'
get_pattern_match('Born.*\n(.*)\(',text).strip()
#'19 April 1957'
get_pattern_match('Parents.*\n(.*)',text)
#'Dhirubhai Ambani (father)'


from PyPDF2 import PdfFileReader
#importing required module
from PyPDF2 import PdfReader
#creating a pdf reader object
reader=PdfReader("C:/1-python/kopargaon-part-1.pdf")
#printing number of pages in pdf file
print(len(reader.pages))
#getting a specific pages from the pdffile
pages=reader.pages[1]
#extracting text from pages
text=pages.extract_text()
print(text)
#data should not be scanned i.e images
##########################################

from PyPDF2 import PdfFileReader
#importing required module
from PyPDF2 import PdfReader
#creating a pdf reader object
reader=PdfReader("C:/1-python/matrix_basics.pdf")
#printing number of pages in pdf file
print(len(reader.pages))
#getting a specific pages from the pdffile
pages=reader.pages[1]
#extracting text from pages
text=pages.extract_text()
print(text)

######################################################

#20JUNE

#extracting info from twitter
import re
sentence5="sharat twitted, wittnessing 68th republic day India from Rajpath,\new Delhi, Mesmorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+', ' ', sentence5).split()

"""
o/p:
['sharat',
 'twitted',
 'wittnessing',
 '68th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 'ew',
 'Delhi',
 'Mesmorizing',
 'performance',
 'by',
 'Indian',
 'Army']    
"""



'''
re.sub(r'([^\s\w]|_)+', ' ', som.......
'''

#extracting n-grams
#n-gram can be extracted using there techniques
#1.
#2.
import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
n_gram_extractor("The cute little boy is playing with kitten",2)
n_gram_extractor("The cute little boy is playing with kitten",3)
"""
['The', 'cute']
['cute', 'little']
['little', 'boy']
['boy', 'is']
['is', 'playing']
['playing', 'with']
['with', 'kitten']
['The', 'cute', 'little']
['cute', 'little', 'boy']
['little', 'boy', 'is']
['boy', 'is', 'playing']
['is', 'playing', 'with']
['playing', 'with', 'kitten']
"""
#############################

#####################################

#1.Extract all twitter handles from following text. Twitter handle
text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern='https://twitter.com/([a-zA-Z0-9_]+)'
re.findall(pattern, text)
"""
o/p:
['elonmusk', 'teslarati', 'dummy_tesla', 'dummy_2_tesla']
"""
####################################
#2.Extract concentration risk types. It will be a text
#that appears 
text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern='Concentration of Risk: ([^\n]*)'
re.findall(pattern, text)
"""
o/p:
    ['Credit Risk', 'Supply Risk']
"""

########################################################
#companies in europe reports their financial numbers of semi annual
#and you can have a document like this. To extract quarterly and
#period you can use a regex as shown below
import re
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'#?:match this
matches=re.findall(pattern,text)
matches
##########################################

text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern='(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text)
matches
"""
o/p:
   ['9991116666', '(999)-333-7777']
"""

text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches = re.findall(pattern,text)
matches
##############################################
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern='Note \d - ([^\n]*)'#([^\n]*) all text before end of line
matches=re.findall(pattern,text)
matches
"""
Out[12]: ['Overview', 'Summary of Significant Accounting Policies']
"""
#do for flipcart text and extract it
#############################################

#Extract financial periods from a company's financial reporting
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text)
matches
"""
Out[13]: ['FY2021 Q1', 'FY2020 Q4']
"""
#########################################
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. fY2020 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern, text, flags=re.IGNORECASE)
matches
"""
Out[15]: ['FY2021 Q1', 'fY2020 Q4']
"""
##########################################
#do limitatization,tokenization,extract title,replace anything i.e words,,remove stock words,create list and do dataframe,extract stari.e review
import re
text='''
Binding: Paperback
Publisher: Na
Genre: Trading, Stock market
ISBN: 9789357599290
Edition: 2022
Pages: 92
'''
pattern='ISBN: \d{13}'
matches=re.findall(pattern,text)
matches
pattern='Genre: ([^\n]*)'
re.findall(pattern, text)
############################################

#21JUNE

import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([^\s\w]|_)+', ' ', input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
n_gram_extractor("The cute little boy is playing with kitten".split(),2)
n_gram_extractor("The cute little boy is playing with kitten".split(),3)  




     
###########################################
        
from nltk import ngrams
#extraction n-grams with nltk
list(ngrams("The cute little boy is playing with kitten".split(),2))
list(ngrams("The cute little boy is playing with kitten".split(),3))
"""
Out[11]: 
[('The', 'cute'),
 ('cute', 'little'),
 ('little', 'boy'),
 ('boy', 'is'),
 ('is', 'playing'),
 ('playing', 'with'),
 ('with', 'kitten')]

Out[12]: 
[('The', 'cute', 'little'),
 ('cute', 'little', 'boy'),
 ('little', 'boy', 'is'),
 ('boy', 'is', 'playing'),
 ('is', 'playing', 'with'),
 ('playing', 'with', 'kitten')]

"""

######################################
from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kitten")
blob.ngrams(n=2)
blob.ngrams(n=3)
"""
Out[14]: 
[WordList(['The', 'cute', 'little']),
 WordList(['cute', 'little', 'boy']),
 WordList(['little', 'boy', 'is']),
 WordList(['boy', 'is', 'playing']),
 WordList(['is', 'playing', 'with']),
 WordList(['playing', 'with', 'kitten'])]

"""
#####################################

######Tokenization using Keras
sentence5="sharat twitted, wittnessing 68th republic day India from Rajpath,\new Delhi, Mesmorizing performance by Indian Army!"
sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)
#(give error find error on stackoverflow)
#######################################
#Tokenizaton using TextBlob
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words
"""
WordList(['sharat', 'twitted', 'wittnessing', '68th',
          'republic', 'day', 'India', 'from', 'Rajpath', 
          'ew', 'Delhi', 'Mesmorizing', 'performance', 
          'by', 'Indian', 'Army'])
"""
############################
#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
"""
['sharat',
 'twitted',
 ',',
 'wittnessing',
 '68th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 ',',
 'ew',
 'Delhi',
 ',',
 'Mesmorizing',
 'performance',
 'by',
 'Indian',
 'Army',
 '!']

"""
###############################################

#Multi-Word_Expression

from nltk.tokenize import MWETokenizer
'''
multi-word tokenizer are eseential for tasks whwer the meaning
of the text hravenly depends on the interpretation of phrases as wholes 
rather than as sums of individual words.For instance,
in sentimemts analysis, recognizing 'not good'
as a single neagtive sentiments unit rather than 'not' and 'good' seperatelly can significantly
affect the outcome
'''
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('!',' ').split())
'''
o/p:
  ['sharat',
   'twitted,',
   'wittnessing',
   '68th',
   'republic_day',
   'India',
   'from',
   'Rajpath,',
   'ew',
   'Delhi,',
   'Mesmorizing',
   'performance',
   'by',
   'Indian',
   'Army']  
    
'''







