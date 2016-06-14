#! /usr/bin/python3.4

import sys

fname = sys.argv[1:2]
files = sys.argv[2:]

if not fname or not files: sys.exit(0)

with open(fname[0],'wb') as fout:
    for n in files:
        with open(n,'rb') as fi:
            fout.write(fi.read())

