#!/usr/bin/env python
#
# This script is for taking the files from:
# http://www.lexically.net/wordsmith/support/shakespeare.html
# and turning them into a simple string of text without stage
# directions and character names etc.
from __future__ import unicode_literals

import codecs
import re
import sys

BOM = u'\ufeff'
junk = re.compile('<[^>]*>')

def reformat_shakespeare(filename):
    output = []
    for line in codecs.open(filename, 'rb', 'UTF-16LE'):
        if line.startswith(BOM):
            line = line[1:]
        line = junk.sub('', line).strip()
        if line:
            output.append(line)
    return ' '.join(output)

def main():
    if len(sys.argv) < 2:
        print 'reformatshakespeare.py <list of files>'
        sys.exit(1)

    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    for f in sys.argv[1:]:
        print reformat_shakespeare(f)

if __name__ == '__main__':
    main()
