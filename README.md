This repository contains code for analyzing the text of Cards Against Humanity cards and attempting to generate new ones from a corpus.

[You can download text files of the original cards here](https://github.com/nodanaonlyzuul/against-humanity).

The `analyzeanswers.py` script attempts to categorize the answer cards (white cards). It currently just groups them by sentence chunking using [the pattern module](http://www.clips.ua.ac.be/pages/pattern)'s parser.

The `makeanswers.py` script takes some text as input and prints phrases from the input that match the categories produced by `analyzeanswers.py`.

For testing I've been using [the WordSmith tools Shakespeare Corpus](http://www.lexically.net/wordsmith/support/shakespeare.html), so `reformatshakespeare.py` can take the text files from that corpus and reformat them as plain text for input into `makeanswers.py`.
