#!/usr/bin/env python
"""mapper.py"""
#~/testdir$ cat articles.txt | ./mapper.py | sort -k1,1 | ./reducer.py

from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

import sys
import re
reload(sys)

sys.setdefaultencoding('utf8')

#ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().decode('utf-8','ignore').encode('utf-8')
    # split the line into words
    #words = line.split()
    words = re.split(r'[,;*." ]', line)
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
	word = word.lower()
	word = word.replace('@',"").replace('"',"").replace('#',"").replace("'s","")
	if "co/" in word:
	    continue
	if "<ed>" in word:
	    continue
   	if word not in stop_words:
	     if word.strip() != "":
		  #word = ps.stem(word)
		  word = lmtzr.lemmatize(word)
                  print '%s\t%s' % (word, 1)
	