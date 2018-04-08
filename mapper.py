#!/usr/bin/env python
"""mapper.py"""

#References: http://www.michael-noll.com/tutorials

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

import sys
import re
reload(sys)

sys.setdefaultencoding('utf8')
stop_words = set(stopwords.words('english'))

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip().decode('utf-8','ignore').encode('utf-8')
    words = re.split(r'[,;*." ]', line)
    for word in words:
       	word = word.lower()
	word = word.replace('@',"").replace('"',"").replace('#',"").replace("'s","").replace(':',"")
	if "co/" in word:
	    continue
	if "<ed>" in word:
	    continue
	if "http" in word:
	    continue
   	if word not in stop_words:
	     if word.strip() != "":
		  word = lmtzr.lemmatize(word)
                  print '%s\t%s' % (word, 1)
	