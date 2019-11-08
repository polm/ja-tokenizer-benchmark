#!/usr/bin/env python 
from fugashi import Tagger
tt = Tagger()
from collections import Counter

wc = Counter()

for line in open('wagahai.txt'):
    for word in tt.parseToNodeList(line.strip()):
        wc[word.surface] += 1
        
