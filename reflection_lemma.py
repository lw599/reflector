# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import sys, nltk, re, pprint, codecs, csv
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
from nltk.corpus import wordnet

#the input files of the reflection corpus and dictionary have to be given as argument, so in terminal what this looks like is python reflection.py reflectiontextfilename.txt reflectionDictionary.txt
with open(sys.argv[1], 'r') as r:
  refl = r.read()

# function to translate part of speech tagging between nltk's pos_tag and the wordnet lemmatizer
def get_wordnet_pos(treebank_tag):
  if treebank_tag.startswith('J'):
    return wordnet.ADJ
  elif treebank_tag.startswith('V'):
    return wordnet.VERB
  elif treebank_tag.startswith('N'):
    return wordnet.NOUN
  elif treebank_tag.startswith('R'):
    return wordnet.ADV
  else:
    return None

#preprocessing
tokens = nltk.wordpunct_tokenize(refl.decode('utf8', 'ignore'))
text = nltk.Text(tokens)
text2 = [w.lower() for w in text if w.isalpha()]

#remove no nor not from stopwords
stopwords = ['it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'be', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'as', 'of', 'at', 'by', 'for', 'with', 'about', 'above', 'below', 'into', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'then', 'here', 'there', 'when', 'where', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'only', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should']

englwords = [w for w in text2 if w not in stopwords]
englwords = nltk.pos_tag(englwords)

with open(sys.argv[2], 'r') as d:
  dictionary = d.read().splitlines()
  
dictionary = nltk.pos_tag(dictionary)

wordnet_lemmatizer = WordNetLemmatizer()

engltextlemmas = []
for w, pos in englwords:
	if get_wordnet_pos(pos):
		engltextlemmas.append(wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(pos)))
	else:
		engltextlemmas.append(wordnet_lemmatizer.lemmatize(w))
        
engldiclemmas = []
for w, pos in dictionary:
	if get_wordnet_pos(pos):
		engldiclemmas.append(wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(pos)))
	else:
		engldiclemmas.append(wordnet_lemmatizer.lemmatize(w))

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

with open('data/output/freq_lemmas.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  for count, word in enumerate(engldiclemmas):
    writer.writerow([word, engltextlemmas.count(word), englfreqlist[count], totalfreq, reflfreqlist[count]])