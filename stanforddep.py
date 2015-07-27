from stanford.corenlp import *
from nltk import *

with open("data/engelhardtest.txt", 'rU') as f:
	engelhard = f.read()
	engelhard2 = engelhard.decode('utf8')
#print(engelhard)

corenlp = StanfordCoreNLP(corenlp_path = "./stanford/stanford-corenlp-full-2014-08-27/")
corenlp.parse(engelhard2)
