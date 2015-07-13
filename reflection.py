# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import sys, nltk, re, pprint, codecs, csv
from nltk.stem.snowball import SnowballStemmer
from nltk import FreqDist

#the output is going to show up in a new txt file called reflectionfreqdist.txt
'''
f = open('data/output/reflectionfreqdist.csv', 'w')
sys.stdout = f
'''

#the input file has to be given as an argument, so in terminal what this looks like is python reflection.py englehardtest.txt or whatever your input file is called
input = open(sys.argv[1], 'r')
refl = input.read()

#preprocessing
tokens = nltk.wordpunct_tokenize(refl.decode('utf8', 'ignore'))
text = nltk.Text(tokens)
englwords = [w.lower() for w in text if w.isalpha()]

#stemming of input text
stemmer = SnowballStemmer("english")
engltextstems = []
for word in englwords:
	engltextstems.append(stemmer.stem(word))

engltextstems = sorted(engltextstems)

#Lara's reflection dictionary
refldic = ['affect', 'after', 'alter', 'application', 'appreciate', 'approach', 'associate', 'attribute', 'aware', 'before', 'brought', 'change', 'choice', 'connect', 'consider', 'contribute', 'cope', 'cura', 'deep', 'develop', 'dilemma', 'effect', 'emotion', 'empathy', 'empower', 'enable', 'encourage', 'enhance', 'establish', 'evaluate', 'experience', 'family', 'forgive', 'forward', 'friend', 'grow', 'grew', 'happy', 'help', 'ignorance', 'impact', 'importance', 'influence', 'internalize', 'learn', 'major', 'meditation', 'mindfullness', 'minor', 'motivate', 'notice', 'objective', 'open-minded', 'open', 'opinion', 'others', 'outlook', 'ownership', 'passion', 'peers', 'perception', 'personality', 'personally', 'perspective', 'preconception', 'prepare', 'privilege', 'pursue', 'reactions', 'realize', 'reflection', 'relationship', 'relevance', 'resolve', 'resonate', 'responsibility', 'self-reflection', 'situation', 'standpoint', 'strength', 'struggle', 'subconsciously', 'success', 'taught', 'teach', 'think', 'unconscious', 'understand', 'unmotivated', 'valuable', 'view', 'viewpoint', 'weakness', 'widen']

#stemming of reflection dictionary
engldicstems = []
for word in refldic:
	engldicstems.append(stemmer.stem(word))

#nltk freqdist
fdistengl = nltk.FreqDist(engltextstems)

#list of frequencies for reflection words
englfreqlist = []
for word in engldicstems:
	englfreq = fdistengl.freq(word)
	englfreqlist.append(englfreq)

#total frequency of all reflection words
totalfreq = sum(englfreqlist)

#frequency of a word in only reflection words (in order to have bigger percentages for individual words)
reflfreqlist = []
for i in englfreqlist:
	reflfreq = i / totalfreq
	reflfreqlist.append(reflfreq)

#output printing here-- will be formatted with each word on a new line, col 1: word, col 2: word count across englehard text, col 3: word frequency across englehard text, col 4: total frequency of all reflection words (unchanging), col 5: frequency of the word among reflection words
'''
count = 0
for word in engldicstems:
	print(word, engltextstems.count(word), englfreqlist[count], totalfreq, reflfreqlist[count])
	count += 1
f.close()
'''

with open('data/output/freq.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  for count, word in enumerate(engldicstems):
    writer.writerow([word, engltextstems.count(word), englfreqlist[count], totalfreq, reflfreqlist[count]])