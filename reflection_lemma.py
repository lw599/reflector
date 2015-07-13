# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import sys, nltk, re, pprint, codecs, csv
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist

#the input files of the reflection corpus and dictionary have to be given as argument, so in terminal what this looks like is python reflection.py reflectiontextfilename.txt reflectionDictionary.txt
with open(sys.argv[1], 'r') as r:
	refl = r.read()

#preprocessing
tokens = nltk.wordpunct_tokenize(refl.decode('utf8'))
text = nltk.Text(tokens)
englwords = [w.lower() for w in text if w.isalpha()]

#lemmatization of input text
wordnet_lemmatizer = WordNetLemmatizer()
engltextlemmas = []
for word in englwords:
	engltextlemmas.append(wordnet_lemmatizer.lemmatize(word))

engltextlemmas = sorted(engltextlemmas)

with open(sys.argv[2], 'r') as d:
	dictionary = d.read().splitlines()

#lemmatization of reflection dictionary
engldiclemmas = []
for word in dictionary:
	engldiclemmas.append(wordnet_lemmatizer.lemmatize(word))
engldiclemmas = sorted(set(engldiclemmas))

#nltk freqdist
fdistengl = nltk.FreqDist(engltextlemmas)

#list of frequencies for reflection words
englfreqlist = []
for word in engldiclemmas:
	englfreq = fdistengl.freq(word)
	englfreqlist.append(englfreq)

#total frequency of all reflection words
totalfreq = sum(englfreqlist)

#frequency of a word in only reflection words (in order to have bigger percentages for individual words)
reflfreqlist = []
for i in englfreqlist:
	reflfreq = i / totalfreq
	reflfreqlist.append(reflfreq)

with open('data/output/freq_stems.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  for count, word in enumerate(engldiclemmas):
    writer.writerow([word, engltextlemmas.count(word), englfreqlist[count], totalfreq, reflfreqlist[count]])
	
f.close()