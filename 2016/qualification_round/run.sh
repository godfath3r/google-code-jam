#!/bin/bash
echo 'Running counting sheep problem'
time python2 A-counting-sheep.py < input_sets/A-small-attempt0.in > A-small-attempt0.out
echo 'Done... A-small-attempt0.out will hold the correct output'
echo 'Running counting sheep problem Large'
time python2 A-counting-sheep.py < input_sets/A-large.in > A-large.out
echo 'Done... A-large.out will hold the correct output'
