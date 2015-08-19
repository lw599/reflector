from stanford_corenlp_pywrapper import CoreNLP
from pprint import pprint
import glob

proc = CoreNLP("coref", corenlp_jars=["stanford/stanford-corenlp-full-2015-04-20/*"])
path = 'data/engelhard/0/'
for filename in glob.glob(path+'101.txt'):
  print(filename)
  with open(filename, 'rU') as f:
    engelhard = f.read()
    engelhard2 = engelhard.decode('utf8', 'ignore')
    print(engelhard2)
    a = proc.parse_doc(engelhard2)
    for n, entity in enumerate(a['entities']):
      # identify the referent by taking the first item in the mentions list
      referent_span = entity['mentions'][0]['tokspan_in_sentence']
      referent_sentence = entity['mentions'][0]['sentence']
      referent_token = a['sentences'][referent_sentence]['tokens'][referent_span[0]:referent_span[1]]
      print referent_token
#      a['sentences'][a['entities'][0]['mentions'][0]['sentence']]['tokens'][a['entities'][0]['mentions'][0]['tokspan_in_sentence'][0]:a['entities'][0]['mentions'][0]['tokspan_in_sentence'][1]]
  #pprint(a)