#!/usr/bin/env python
from sudachipy import dictionary, tokenizer
from collections import Counter

# Use fine-grained tokenization since it's most similar to Unidic used by other
# tokenizers
mode = tokenizer.Tokenizer.SplitMode.A
tokenizer_obj = dictionary.Dictionary().create(mode=mode)

wc = Counter()

for line in open('wagahai.txt'):
    for word in tokenizer_obj.tokenize(line.strip()):
        wc[word.surface] += 1
