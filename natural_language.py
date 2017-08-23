from collections import Counter
from itertools import chain
from nltk.corpus import brown
from nltk import sent_tokenize
from nltk.tokenize import ToktokTokenizer
import math


def top_frequencies(frequencies, percentage=1):
    # Find out how frequently a word should come up to be included
    full = sorted(frequencies.values(), reverse=True)
    frequency = len(full) * (percentage/100)
    print("Top %age only contains words that occurred " + str(math.ceil(frequency)) + " times or more.")

    # If a word comes up this amount of times or more, add it to a new dictionary
    top = {}
    for key in frequencies.keys():
        if frequencies[key] >= frequency:
            top[key] = frequencies[key]

    return top


def word_frequencies(contents, percent=100):
    toktok = ToktokTokenizer()
    string_corpus = brown.raw()

    # Frequencies for each file
    list = []
    for file in contents.keys():
        tokenised = [toktok.tokenize(sent) for sent in sent_tokenize(string_corpus)]
        fdist = Counter(chain(*tokenised))
        list.append(fdist)

    # Combine keys into one set, eliminating duplicates
    keys = []
    for sublist in list:
        keys += sublist
    keys = set(keys)

    # Build combined frequency dict
    frequencies = {}
    for key in keys:
        total = 0
        for sublist in list:
            if key in sublist.keys():
                total += sublist[key]
        frequencies[key] = total
    print("Total words: " + str(len(frequencies.keys())))

    return frequencies
