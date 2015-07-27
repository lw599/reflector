'''
clean-entries.py

This script does the following:
1. Identifies user IDs that occur more than a minimum number of times in the data file.
2. Keeps only entries from those users and discards the rest.
3. Processes the text of the remaining entries to remove extra spaces and HTML tags.
4. Outputs the resulting entries to a new file.
'''

import sys, csv

with open(sys.argv[1], 'rU') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    print row[0]