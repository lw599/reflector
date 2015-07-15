import csv, nltk
from random import shuffle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

CODING = {
  '0': 'self, surface',
  'B': 'self, deep',
  'A': 'world/domain, surface',
  'X': 'world/domain, deep',
}

#read in the data
categories = {}
with open('data/384_rated.tsv', 'rb') as f:
  reader = csv.reader(f, delimiter="\t")
  for row in reader:
    #print row[0], row[1]
    # create the category if it doesn't already exist in the dictionary
    if row[0] not in categories.keys():
      categories[row[0]] = []
    # assign this row to the appropriate category
    categories[row[0]].append(row[1])

'''
data
  integration
    self
    domain
  depth
    surface
    deep
'''

data = {
  'integration': {},
  'depth': {},
}
data['integration']['self'] = categories['0'] + categories['B']
data['integration']['domain'] = categories['A'] + categories['X']
data['depth']['surface'] = categories['0'] + categories['A']
data['depth']['deep'] = categories['B'] + categories['X']

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

def cndls_classify(categories):
  # print a summary of the different categories
  for k, v in categories.items():
    print k, len(v), len(v)/3

  print CODING

  # create the different sets for the classifier
  # for now, we're just going to go with surface and deep
  # simplification, but: 0 and X

  reflection_set = {}
  # first, randomly select a third of each category
  for k, v in categories.items():
    shuffle(categories[k]) # shuffle all categories
    # if the reflection set key doesn't exist, create it
    if k not in reflection_set.keys():
      reflection_set[k] = []
  #  category_set = categories[k][:len(categories[k])/3] # assign to reflection sets
    category_set = categories[k][:len(categories[k])] # assign to reflection sets
    for reflection in category_set:
      reflection_set[k].append((reflection.decode('utf8', 'ignore'), k))

  '''
  text2 = nltk.wordpunct_tokenize(text.decode('utf8', 'ignore'))
  text3 = [w.lower() for w in text2 if w.isalpha()]

  stopwords = stopwords.words('english')
  stopwords = stopwords + ['m', 'll', 'd', 's', 've', 're']
  final = [w for w in text3 if w not in stopwords]
  '''

  '''
  #lemmatization of input text
  wordnet_lemmatizer = WordNetLemmatizer()
  engltextlemmas = []
  for word in englwords:
    engltextlemmas.append(wordnet_lemmatizer.lemmatize(word))
  '''

  reflections = []
  for (words, sentiment) in reflection_set['self'] + reflection_set['domain']:
    #words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    text2 = nltk.wordpunct_tokenize(words)
    text3 = [w.lower() for w in text2 if w.isalpha()]
    stopwords = ['it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these those', 'am', 'is are', 'was were', 'be been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'as', 'of', 'at', 'by', 'for', 'with', 'about', 'above', 'below', 'into', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'then', 'here', 'there', 'when', 'where', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should']
    text4 = [w for w in text3 if w not in stopwords]
    text5 = nltk.pos_tag(text4)

    # lemmatize!
    wordnet_lemmatizer = WordNetLemmatizer()
    words_filtered = []
    for w, pos in text5:
      if get_wordnet_pos(pos):
        words_filtered.append(wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(pos)))
      else:
        words_filtered.append(wordnet_lemmatizer.lemmatize(w))
    #print words_filtered
    reflections.append((words_filtered, sentiment))

  def get_words_in_reflections(reflections):
    all_words = []
    for (words, sentiment) in reflections:
      all_words.extend(words)
    return all_words
  def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
  
  word_features = get_word_features(get_words_in_reflections(reflections))

  def extract_features(document):
      document_words = set(document)
      features = {}
      for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
      return features
    
  training_set = nltk.classify.util.apply_features(extract_features, reflections)

  # print training_set

  classifier = nltk.NaiveBayesClassifier.train(training_set)

  def train(labeled_featuresets, estimator=nltk.probability.ELEProbDist):
      # Create the P(label) distribution
      label_probdist = estimator(label_freqdist)
      # Create the P(fval|label, fname) distribution
      feature_probdist = {}
      return NaiveBayesClassifier(label_probdist, feature_probdist)

  # print label_probdist.prob('deep')
  # print label_probdist.prob('surface')

  # print feature_probdist
  # print feature_probdist[('deep', 'contains(opened)')].prob(True)

  print classifier.show_most_informative_features(50)
  # show_most_informative_features

cndls_classify(data['integration'])