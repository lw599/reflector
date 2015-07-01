Reflector
=========

Initial setup
-------------
* Clone the repository and add a ``data`` folder in the project root.
* Place a file called ``corpus.csv`` in the ``data`` folder.
* Create a directory called ``output`` in the ``data`` folder.
* From the project root, run ``python export-text.py``. This takes the ``corpus.csv`` file and splits it into individual text files that are stored in the ``data/output`` folder.

Creating the corpus
-------------------
* From the Python interactive shell, run the following commands:
```
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
newcorpus = PlaintextCorpusReader('data/output/', '.*')
```
* This will create an NLTK corpus called ``newcorpus``.
