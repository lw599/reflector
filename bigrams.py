from __future__ import division
from __future__ import print_function
import sys, nltk, re, pprint, codecs, csv
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
from nltk.collocations import *

with open(sys.argv[1], 'rU') as f:
	engltext = f.read()
	
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

#remove no nor not from stopwords
stopwords = ['it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'be', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'as', 'of', 'at', 'by', 'for', 'with', 'about', 'above', 'below', 'into', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'then', 'here', 'there', 'when', 'where', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'only', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'i', 'me', 'my', 'myself', 'you', 'your', 'yourself', 'we', 'us', 'ourselves', 'ourself', 'll', 've', 'd', 're', 'm']

#preprocessing
tokens = nltk.wordpunct_tokenize(engltext.decode('utf8'))
text = nltk.Text(tokens)
englwords = [w.lower() for w in text if w.isalpha()]
englwords = [w for w in englwords if w not in stopwords]
englwords = nltk.pos_tag(englwords)

#lemmatization of input text
wordnet_lemmatizer = WordNetLemmatizer()

engltextlemmas = []
for w, pos in englwords:
	if get_wordnet_pos(pos):
		engltextlemmas.append(wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(pos)))
	else:
		engltextlemmas.append(wordnet_lemmatizer.lemmatize(w))
	
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

bgmfinder = BigramCollocationFinder.from_words(engltextlemmas, window_size=5)
bgmfinder.apply_freq_filter(10)

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