#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        print '%s\t%s' % (word, "1")

    # remove stopwords
    for word in words:
	if word not in stopwords:
		print word

    # sklearn for list of stopwords
    from sklearn.feature_extraction import stop_words
    stops = set(stop_words.ENGLISH_STOP_WORDS)

    # lowercase the text before removing stopwords
    line = line.strip().lower()

    # remove punctuation
    s.translate(str.maketrans('', '', string.punctuation))
