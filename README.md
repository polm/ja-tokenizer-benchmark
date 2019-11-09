# Tokenizer Benchmarks

This repository has scripts for benchmarking Japanese tokenizers. It was
originally created to make sure that [fugashi](https://github.com/polm/fugashi)
wasn't slower than [mecab-python3](https://github.com/samurait/mecab-python3). 

The benchmark task is to get a per-word word count from the [Aozora Bunko edition of "I am a Cat"](https://www.aozora.gr.jp/cards/000148/files/789_14547.html), stored in the `wagahai.txt` file, using a Counter object.

I suggest using [hyperfine](https://github.com/sharkdp/hyperfine) for
benchmarking, though anything that can run the scripts is adequate.

To run:

    # install mecab, unidic, and hyperfine with your OS package manager
    pip install fugashi mecab-python3 sudachipy
    # sudachipy needs its own dictionary
    pip install https://object-storage.tyo2.conoha.io/v1/nc_2520839e1f9641b08211a5c85243124a/sudachi/SudachiDict_core-20191030.tar.gz
    hyperfine -w 10 ./bench*.py

Results on my machine:

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `./benchmark-fugashi.py` | 266.4 ± 1.2 | 264.4 | 268.3 | 1.0 |
| `./benchmark-mecab-python3.py` | 259.2 ± 5.3 | 253.5 | 270.2 | 1.0 |
| `./benchmark-sudachi.py` | 58027.6 ± 234.0 | 57658.2 | 58504.6 | 223.8 |
