'''
Usage: python counter.py [data file] [output file]

Sample: python counter.py data/open-assessment-per-user-with-scores.csv |more

This script takes self assessments from an edX course and scores the text based on key concepts taken from the model answer given.
'''

import csv, sys, re

'''
def process(answer):
  #preprocessing
  tokens = nltk.wordpunct_tokenize(answer.decode('utf8', 'ignore'))
  text = nltk.Text(tokens)
  words = [w.lower() for w in text if w.isalpha()]

  #stemming of input text
  #stemmer = SnowballStemmer("english")
  #textstems = []
  #for word in words:
  #  textstems.append(stemmer.stem(word))

  #textstems = sorted(textstems)
  return textstems
'''

#TODO: Create a lookup dictionary of "approved" words for each assessment.
#How do we handle the set phrases? -> Maybe list them separate from the other terms and search for them in the answer pre-stemming?
approved = {
  3: [r'\blaw\w*\b', r'\bprosecut\w*\b', r'International Criminal Court', r'\bsanction\w*\b', (r'U\W?N\W?|Security Council', r'military|force')],
  4: ['patterns', 'simplicity', 'operations', 'personnel', 'recruitment', 'fundraising', 'existing', 'old', 'current', 'technology', 'commercial', 'trace', 'incriminating'],
  5: ['hide', 'population', 'casualties', 'suffer', 'popular', 'goals', 'compelled', 'irrelevant', 'recruits', 'money'],
  6: ['Preamble', 'security', 'Union', 'Constitution', 'powers', 'Congress', 'President', 'POTUS', 'defense', 'welfare', 'commerce', 'nations', 'piracies', 'felons', 'declare war', 'marque', 'reprisal', 'army', 'Navy', 'naval', 'militia', 'insurrections', 'invasions', 'Commander in Chief', 'Senate', 'treaties', 'Youngstown'],
  7: ['status', 'operational network', 'mission', 'self-defense', 'control', 'attack', 'damage', 'recruit', 'fundraise', 'resource', 'targeting', 'goals'],
  8: ['Afghanistan', 'Pakistan', 'Sudan', 'train', 'plan', 'organize', 'army', 'insurgencies', 'attack', 'counterterrorist', 'loss', 'constituents', 'regime', 'Hamas', 'Hizbollah'],
  9: ['wrong', 'mindless', 'neutral', 'indiscriminately', 'rules', 'misguided', 'evil', 'corrupt', 'redemption', 'cause', 'Manichean', 'innocent', 'freedom', 'murderous', 'criminal', 'civilian'],
  10: ['enemy', 'vulnerabilities', 'democratic', 'regime', 'vulnerable', 'attrition', 'strategy', 'loss', 'soldiers', 'cost', 'war', 'withdrawal', 'insurgency', 'propaganda of the deed', 'violence', 'Lone Wolf', 'Spoiler', 'negotiations', 'mass'],
  11: ['jihad', 'weapon', 'Sunni', 'Shii', 'forbidden', 'martyrdom', '1983 Hezbollah U.S. Marine Barracks bombing', ' Palestinian intifada', 'power', 'tactic', 'debate', 'civilians', 'Islamic law'], 
  13: ['movement', 'Pakistan', 'arguments', 'British', 'decolonize', 'Asia', 'Muslims', 'Hindus', 'autonomous', 'state', 'nation-state', 'partition', 'Muslim League', 'Indian National Congress', 'ideology', 'struggle', 'legitimacy', 'India'],
  14: ['independence', 'constitution', 'Usmani', 'movement', 'Pakistan', 'Khan', 'assembly', '1949', 'ideologically', 'Islamic state', 'preamble', 'secular', 'Allah', 'legislators', 'democracy', 'freedom', 'equality', 'tolerance', 'justice', 'Muslims', 'Quran', 'Sunnah'],
  15: ['French', 'France', 'positive', 'connotation', 'social order', 'fear', 'state', 'sub-state', 'anarchist', 'anti-monarchical', 'revolutionary', 'movements', '1900s', 'separatist', '20th century', 'Nazi', 'USSR', 'Stalin', 'repressive', '1950s', 'rebels', 'nationalists', 'anti-colonialist', '1980s', 'extremist', 'radical', 'religious', 'fanatic', '21st century', 'sponsor', 'negative', 'abolish', 'perpetrator', 'victim'],
  16: ['Sunni', 'Salafism', 'rebel', 'ruler', 'Muslim', 'unbeliever', 'sharia', 'resistance', 'Salafis'],
  17: ['1974', 'Bhutto', 'critics', 'non-Muslim', 'Pakistan', 'finality', 'Prophet', 'living', 'apostate', 'quotidian', 'religious', 'Quran', 'kill', 'murder', 'movement'],
  18: ['proliferation', 'Kapur', 'subcontinent', 'low-intensity', 'conflict', 'Ganguly', 'deterrent', 'comparison', 'Pakistan', 'Islamic', 'militants', 'impunity', 'punitive', 'conventional', 'India', 'Indo-Pakistan', 'war', 'terrorist'],
  19: ['IL', 'traditionally', 'states', 'countries', 'actors', 'system', 'persons', 'non-state', 'participants', 'rights', 'responsibilities', 'inadequate', 'mechanisms', 'creating', 'implementing', 'rules', 'situations', 'swift', 'global', 'politics', 'definition', 'cases']
}
'''
# stem the approved dictionary
with open(sys.argv[2], 'r') as f:
  approved = f.read()
  stemmed_approved = process(approved)
  print stemmed_approved
'''
# stem the answers
# TODO: make sure we look up the proper assessment list for each item! right now it's just going off the assessment4.txt file.
with open(sys.argv[1], 'r') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    assessment = row[1]
    final = {}
    answer = row[3]
    for regex in approved[3]:
      print re.findall(regex,answer)
'''
    #result = process(answer)
    intersected_words = list(set(result) & set(stemmed_approved))
    print intersected_words
'''    
'''
    words = nltk.tokenize.word_tokenize(answer)
    fdist = FreqDist(words)
    for k, v in fdist.items():
      if k in approved:
        final[k] = v
'''