#!/usr/bin/env python
from __future__ import unicode_literals
from pattern.en import parsetree, parse
import codecs
import os
import sys
from collections import defaultdict
import HTMLParser
# https://github.com/nodanaonlyzuul/against-humanity
SOURCE = '../against-humanity'

def main():
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    d = defaultdict(list)
    p = HTMLParser.HTMLParser()
    for line in codecs.open(os.path.join(SOURCE, 'answers.txt'), 'rb', 'utf-8'):
        line = p.unescape(line)
        #print "-----------------------"
        for sentence in parsetree(line):
            d[" ".join(chunk.type for chunk in sentence.chunks)].append(line)
            #for chunk in sentence.chunks:
            #    print chunk.type, [(w.string, w.type) for w in chunk.words]
    for k, sentences in sorted(d.items(), key=lambda x: len(x[1]), reverse=True):
        print "% 3d %s" % (len(sentences), k)
        print "\t", "\t".join(sentences)

if __name__ == '__main__':
    main()
