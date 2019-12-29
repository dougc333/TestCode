#!/bin/bash

rm -rf loghelix/
python main.py --fasta "helix.fasta" --logdir "logdir/" --nsims 1 --nfrags 3

