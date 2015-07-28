from stanford_corenlp_pywrapper import CoreNLP
from nltk import *

with open("data/engelhardtest.txt", 'rU') as f:
	engelhard = f.read()
	engelhard2 = engelhard.decode('utf8')
#print(engelhard)

proc = CoreNLP("parse", corenlp_jars=["stanford/stanford-corenlp-full-2014-08-27/*"])
trees = proc.parse_doc(engelhard2)

print(trees)
