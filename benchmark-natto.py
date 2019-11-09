#!/usr/bin/env python
from natto import MeCab
from collections import Counter

nm = MeCab()
wc = Counter()

for line in open('wagahai.txt'):
    for word in nm.parse(line.strip(), as_nodes=True):
        wc[word.surface] += 1
