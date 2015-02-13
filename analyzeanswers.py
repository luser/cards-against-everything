#!/usr/bin/env python
from __future__ import unicode_literals

import argparse
import codecs
import HTMLParser
import os
import sys

from collections import defaultdict
from pattern.en import parsetree, parse

# https://github.com/nodanaonlyzuul/against-humanity
SOURCE = '../against-humanity'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true', default=False)
    parser.add_argument('--min-occurrences', type=int, default=None)
    args = parser.parse_args()
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    d = defaultdict(list)
    p = HTMLParser.HTMLParser()
    for line in codecs.open(os.path.join(SOURCE, 'answers.txt'), 'rb', 'utf-8'):
        line = p.unescape(line.rstrip())
        #print "-----------------------"
        for sentence in parsetree(line):
            d[" ".join(chunk.type for chunk in sentence.chunks)].append(line)
            #for chunk in sentence.chunks:
            #    print chunk.type, [(w.string, w.type) for w in chunk.words]
    for k, sentences in sorted(d.items(), key=lambda x: len(x[1]), reverse=True):
        if args.min_occurrences is not None and len(sentences) < args.min_occurrences:
            break
        if args.verbose:
            print ("% 3d" % len(sentences)),
        print k
        if args.verbose:
            print "\t", "\n\t".join(sentences)

if __name__ == '__main__':
    main()
