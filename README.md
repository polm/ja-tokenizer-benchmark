# Tokenizer Benchmarks

This repository has scripts for benchmarking Japanese tokenizers. It was
originally created to make sure that [fugashi](https://github.com/polm/fugashi)
wasn't slower than [mecab-python3](https://github.com/samurait/mecab-python3). 

The benchmark task is to get a per-word word count from the [Aozora Bunko edition of "I am a Cat"](https://www.aozora.gr.jp/cards/000148/files/789_14547.html), stored in the `wagahai.txt` file, using a Counter object.

I suggest using [hyperfine](https://github.com/sharkdp/hyperfine) for
benchmarking, though anything that can run the scripts is adequate.

To run:

    # install hyperfine with your OS package manager
    pip install -r requirements.txt
    # benchmark
    hyperfine -w 10 ./bench*.py

Results on my machine:

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `./benchmark-fugashi.py` | 332.0 ± 6.2 | 324.6 | 344.2 | 1.00 |
| `./benchmark-mecab-python3.py` | 353.7 ± 4.4 | 347.1 | 360.0 | 1.07 ± 0.02 |
| `./benchmark-sudachi.py` | 662.0 ± 7.9 | 652.2 | 680.5 | 1.99 ± 0.04 |
| `./benchmark-natto.py` | 1119.2 ± 16.6 | 1095.6 | 1148.7 | 3.37 ± 0.08 |
