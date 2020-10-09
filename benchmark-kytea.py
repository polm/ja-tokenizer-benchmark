#!/usr/bin/env python
import Mykytea
from collections import Counter

tok = Mykytea.Mykytea("-deftag UNKNOWN!!")
wc = Counter()

for line in open('wagahai.txt'):
    for word in tok.getWS(line.strip()):
        wc[word] += 1
