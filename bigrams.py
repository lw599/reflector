from __future__ import division
from __future__ import print_function
import sys, nltk, re, pprint, codecs, csv
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
from nltk.collocations import *

with open(sys.argv[1], 'rU') as f:
	engltext = f.read()
	
#preprocessing
tokens = nltk.wordpunct_tokenize(engltext.decode('utf8'))
text = nltk.Text(tokens)
englwords = [w.lower() for w in text if w.isalpha()]

#lemmatization of input text
wordnet_lemmatizer = WordNetLemmatizer()
engltextlemmas = []
for word in englwords:
	engltextlemmas.append(wordnet_lemmatizer.lemmatize(word))
	
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

bgmfinder = BigramCollocationFinder.from_words(engltextlemmas, window_size=5)
ignoredwords = nltk.corpus.stopwords.words('english')
bgmfinder.apply_freq_filter(3)
bgmfinder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignoredwords)

scored = bgmfinder.score_ngrams(bigram_measures.raw_freq)

with open('data/output/bigramslist.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(sorted(bigram for bigram, score in scored))

with open('data/output/bigramsfreq.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(bgmfinder.ngram_fd.viewitems())

# tgmfinder = TrigramCollocationFinder.from_words(engltextlemmas, window_size=3)
# ignoredwords = nltk.corpus.stopwords.words('english')
# tgmfinder.apply_freq_filter(3)
# tgmfinder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignoredwords)
# 
# with open('data/output/trigrams.csv', 'wb') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerows(tgmfinder.ngram_fd.viewitems())