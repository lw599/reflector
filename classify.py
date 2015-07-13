import csv, nltk

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

for k, v in categories.items():
  print k, len(v), len(v)/3