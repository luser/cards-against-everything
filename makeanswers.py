#!/usr/bin/env python
from __future__ import unicode_literals

import codecs
import fileinput
import operator
import sys

from collections import defaultdict
from pattern.en import parsetree
from pattern.search import search, Pattern

# python analyzeanswers.py --min-occurrences=10
# Arbitrarily cut off at patterns with >10 card examples.
answer_formats = [
    'NP',
    'NP PP NP',
    'VP NP',
    'NP NP',
    'VP NP PP NP',
    'VP PP NP',
    'NP VP NP',
    'NP VP',
    'VP',
]
patterns = dict((s, Pattern.fromstring(s)) for s in answer_formats)

def process(line, results):
    line = line.rstrip()
    t = parsetree(line)
    for k, p in patterns.iteritems():
        matches = search(p, t)
        if k == 'NP': # special-case this
            matches = [m for m in matches if len(m.words) > 1 or m.words[0].tag.startswith('NNP')]
        for m in matches:
            results[k][m.string] += 1

def main():
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    results = defaultdict(lambda: defaultdict(int))
    for line in fileinput.input():
        process(line, results)
    for f in answer_formats:
        found = results[f]
        print "% 3d %s" % (len(found), f)
        print "\t", "\n\t".join(k for k, v in sorted(found.items(), key=operator.itemgetter(1), reverse=True))

if __name__ == '__main__':
    main()
