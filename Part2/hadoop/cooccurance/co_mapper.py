#!/usr/bin/env python
"""co_mapper.py"""

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

import sys
import re
reload(sys)

sys.setdefaultencoding('utf8')

def all_pairs(items):
    pairs_l = []
    nitems = len(items)
    for i1 in items:
        for i2 in items:
	    if i1 != i2:
		str = i1 + "-" + i2
                pairs_l.append(str)
    #print(pairs_l)
    return pairs_l


stop_words = set(stopwords.words('english'))

top_words = ['admistration','amazon','brown','census','deportation','donald','immigrant','service','syria','trump','white']
wpairs = all_pairs(top_words)


# input comes from STDIN (standard input)

for line in sys.stdin:
    line = line.strip().decode('utf-8','ignore').encode('utf-8')
    words = re.split(r'[,;*." ]', line)
    for word in words:
       	word = word.lower()
	word = word.replace('@',"").replace('"',"").replace('#',"").replace("'s","")
	if "co/" in word:
	    continue
	if "<ed>" in word:
	    continue
	if "http" in word:
	    continue
       	if word not in stop_words:
	     if word.strip() != "":
		  word = lmtzr.lemmatize(word)
	if word in top_words:	  
             for word2 in words:
	     	  if word2 not in stop_words:
	               if word2.strip() != "":   
		       	   word2 = lmtzr.lemmatize(word2)
		  if word2 in top_words:
		       w_pair = word + "-" + word2
		       if w_pair in wpairs:
		           print(w_pair + "\t" + "1")