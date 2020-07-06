# Tokenizer Benchmarks

This repository has scripts for benchmarking Japanese tokenizers. It was
originally created to make sure that [fugashi](https://github.com/polm/fugashi)
wasn't slower than [mecab-python3](https://github.com/samurait/mecab-python3). 

The benchmark task is to get a per-word word count from the [Aozora Bunko edition of "I am a Cat"](https://www.aozora.gr.jp/cards/000148/files/789_14547.html), stored in the `wagahai.txt` file, using a Counter object.

I suggest using [hyperfine](https://github.com/sharkdp/hyperfine) for
benchmarking, though anything that can run the scripts is adequate.

To run:

    # install hyperfine with your OS package manager
    pip install install -r requirements.txt
    # benchmark
    hyperfine -w 10 ./bench*.py

The difference between `fugashi` and `fugashi-parse` is that `fugashi-parse`
uses MeCab's `parse` method to get a string and then splits it on whitespace,
while `fugashi` uses the `Node` interface to get a list of word objects.

Results on my machine:

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `./benchmark-fugashi-parse.py` | 245.6 ± 1.3 | 244.3 | 248.9 | 1.00 |
| `./benchmark-fugashi.py` | 268.6 ± 1.2 | 267.6 | 272.1 | 1.09 ± 0.01 |
| `./benchmark-janome.py` | 14897.3 ± 353.1 | 14603.0 | 15733.1 | 60.65 ± 1.47 |
| `./benchmark-mecab-python3.py` | 269.7 ± 6.3 | 265.2 | 286.3 | 1.10 ± 0.03 |
| `./benchmark-natto.py` | 1066.9 ± 9.5 | 1049.4 | 1083.3 | 4.34 ± 0.04 |
| `./benchmark-sudachi.py` | 9187.1 ± 54.2 | 9118.6 | 9306.5 | 37.40 ± 0.29 |
