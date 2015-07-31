from stanford_corenlp_pywrapper import CoreNLP
from pprint import pprint
import os

proc = CoreNLP("coref", corenlp_jars=["stanford/stanford-corenlp-full-2015-04-20/*"])
path = 'data/engelhard/0/'
for filename in os.listdir(path):
  with open(path+filename, 'rU') as f:
    engelhard = f.read()
    engelhard2 = engelhard.decode('utf8', 'ignore')
  a = proc.parse_doc(engelhard2)['entities']
  pprint(a)

