# Tokenizer Benchmarks

This repository has scripts for benchmarking Japanese tokenizers. It was
originally created to make sure that [fugashi](https://github.com/polm/fugashi)
wasn't slower than [mecab-python3](https://github.com/samurait/mecab-python3). 

I suggest using [hyperfine](https://github.com/sharkdp/hyperfine) for
benchmarking, though anything that can run the scripts is adequate.

To run:

    # install mecab, hyperfine with your OS package manager
    pip install fugashi mecab-python3
    hyperfine -w 10 ./bench*.py
