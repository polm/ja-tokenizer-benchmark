#!/usr/bin/env python
import nagisa
from collections import Counter

wc = Counter()

for line in open('wagahai.txt'):
    for word in nagisa.tagging(line.strip()).words:
        wc[word] += 1
