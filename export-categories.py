import csv

with open('data/384_rated.tsv', 'rU') as f:
  reader = csv.reader(f, delimiter="\t")
  for i, row in enumerate(reader):
    f = open('data/' + str(row[0]) + '/' + str(i) + '.txt', 'w')
    f.write(row[1].decode('ascii', 'ignore'))
    f.close()