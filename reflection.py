# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import sys, nltk, re, pprint, codecs, csv
from nltk.stem.snowball import SnowballStemmer
from nltk import FreqDist

#the input file for reflections and reflection dictionary have to be given as first and second arguments respectively, so in terminal what this looks like is python reflection.py englehardtest.txt reflectionDictionary.txt

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
with open(sys.argv[2], 'r') as d:
	dictionary = d.read().splitlines()

#stemming of reflection dictionary
engldicstems = []
for word in dictionary:
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

with open('data/output/freq_stems.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  for count, word in enumerate(engldicstems):
    writer.writerow([word, engltextstems.count(word), englfreqlist[count], totalfreq, reflfreqlist[count]])