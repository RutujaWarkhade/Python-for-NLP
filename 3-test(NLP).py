# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:07:34 2024

@author: om
"""

"""
1. Write a python NLTK program to split the text sentence/paragraph into 
a list of words. 
text = ''' 
Joe waited for the train. The train was late.  
Mary and Samantha took the bus.  
I looked for Mary and Samantha at the bus station. 
''' 
"""
text = '''Joe waited for the train.
The train was late.  
Mary and Samantha took the bus.  
I looked for Mary and Samantha at the bus station. 
'''
a=text.split(" ")
print(a)


"""
2. Write a python program to extract word mention someone in tweets 
using @ from the specified column of a given DataFrame. 
DataFrame: ({ 
'tweets': ['@Obama says goodbye','Retweets for @cash','A political endorsement in 
@Indonesia', '1 dog = many #retweets', 'Just a simple #egg'] 
})
"""
import pandas as pd
import re
data={ 'tweets': ['@Obama says goodbye','Retweets for @cash',
                  'A political endorsement in @Indonesia', 
                  '1 dog = many #retweets', 'Just a simple #egg'] }
df = pd.DataFrame(data)
df

for tweet in df['tweets']:
    for matches in re.findall(r'@(\w+)', tweet):
        print(matches)
        
