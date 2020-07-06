#!/usr/bin/env python
from janome.tokenizer import Tokenizer
from collections import Counter

tok = Tokenizer()
wc = Counter()

for line in open('wagahai.txt'):
    for word in tok.tokenize(line.strip()):
        wc[word.surface] += 1
