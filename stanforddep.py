from __future__ import print_function

from stanford_corenlp_pywrapper import CoreNLP
from nltk import *
import os

proc = CoreNLP("parse", corenlp_jars=["stanford/stanford-corenlp-full-2015-04-20/*"])

#correct subdirectory by coded type goes here
#comment all this to do a single text file instead of a directory
path = 'data/engelhard/A/'
for filename in os.listdir(path):
  print(filename)
  with open(path+filename, 'rU') as f:
    engelhard = f.read()
    engelhard2 = engelhard.decode('utf8', 'ignore')
    trees = proc.parse_doc(engelhard2)
  #  print(engelhard2)

  #this is set as parse (parsing with named entity recognition) but you can also change it to different options, like:
  #ssplit for tokenization and sentence splitting
  #pos for pos and lemmas
  #ner for pos and ner and lemmas
  #parse for pos, lemmas, trees, dependencies
  #nerparse for parsing with ner, pos, lemmas, dependencies
  #coref for coreference including constituent parsing

  #comment this to do coref
  trees = proc.parse_doc(engelhard2)
  #print(trees)

  #uncomment this to do coref
  # proc = CoreNLP("coref", corenlp_jars=["stanford/stanford-corenlp-full-2014-08-27/*"])
  # coref = proc.parse_doc(engelhard2)
  # print(coref)

#uncomment this to do a single text file instead of a directory
#with open("data/engelhardtest.txt", 'rU') as f:
#  engelhard = f.read()
#  engelhard2 = engelhard.decode('utf8')
#print(engelhard)
#this is set as parse (parsing with named entity recognition) but you can also change it to different options, like:
#ssplit for tokenization and sentence splitting
#pos for pos and lemmas
#ner for pos and ner and lemmas
#parse for pos, lemmas, trees, dependencies
#nerparse for parsing with ner, pos, lemmas, dependencies
#coref for coreference including constituent parsing
#comment this to do coref
# proc = CoreNLP("parse", corenlp_jars=["stanford/stanford-corenlp-full-2014-08-27/*"])
# trees = proc.parse_doc(engelhard2)
# print(trees)
#uncomment this to do coref
# proc = CoreNLP("coref", corenlp_jars=["stanford/stanford-corenlp-full-2014-08-27/*"])
# coref = proc.parse_doc(engelhard2)
# print(coref)

#make print statement as argument in command!
