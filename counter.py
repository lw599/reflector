'''
Usage: python counter.py [data file] [output file]

Sample: python counter.py data/open-assessment-per-user-with-scores.csv data/assessment4.txt |more

This script takes self assessments from an edX course and scores the text based on key concepts taken from the model answer given.
'''

import nltk, csv, sys, re
from nltk import FreqDist
from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer

def process(answer):
  #preprocessing
  tokens = nltk.wordpunct_tokenize(answer.decode('utf8', 'ignore'))
  text = nltk.Text(tokens)
  words = [w.lower() for w in text if w.isalpha()]

  #stemming of input text
  stemmer = SnowballStemmer("english")
  textstems = []
  for word in words:
    textstems.append(stemmer.stem(word))

  #textstems = sorted(textstems)
  return textstems

'''
TODO: Create a lookup dictionary of "approved" words for each assessment.
approved = {
  1: ['approved', 'blah', 'third'],
  2: [
}
'''

# stem the approved dictionary
with open(sys.argv[2], 'r') as f:
  approved = f.read()
  stemmed_approved = process(approved)
  print stemmed_approved

# stem the answers
# TODO: make sure we look up the proper assessment list for each item! right now it's just going off the assessment4.txt file.
with open(sys.argv[1], 'r') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    assessment = row[1]
    final = {}
    answer = row[3]
    result = process(answer)
    intersected_words = list(set(result) & set(stemmed_approved))
    print intersected_words
    
    '''
    words = nltk.tokenize.word_tokenize(answer)
    fdist = FreqDist(words)
    for k, v in fdist.items():
      if k in approved:
        final[k] = v
    '''