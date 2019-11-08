#!/usr/bin/env python
from MeCab import Tagger
tt = Tagger()
from collections import Counter

wc = Counter()

for line in open('wagahai.txt'):
    node = tt.parseToNode(line.strip())
    while node:
        #print(node.surface[:node.length], node.feature.split(','))
        wc[node.surface[:node.length]] += 1
        node = node.next


