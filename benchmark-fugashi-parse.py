#!/usr/bin/env python 
from fugashi import Tagger
tt = Tagger('-Owakati')
from collections import Counter

wc = Counter()

for line in open('wagahai.txt'):
    for word in tt.parse(line.strip()).split(' '):
        wc[word] += 1
 
