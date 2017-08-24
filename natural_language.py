from collections import Counter
from itertools import chain
from nltk.corpus import brown
from nltk import sent_tokenize
from nltk.tokenize import ToktokTokenizer
import math


def top_frequencies(frequencies, number=None, percentage=None):
    """
    Find the x most common words where x is either a fixed number or a percentage of the total words.
    If percentage is set to an integer or float, returns the top p% of words and how often they occur.
    If percentage is not set to an integer or float and number is set to an integer, returns the top n words and how
    often they occur.
    """

    words = sorted(frequencies, reverse=True, key=frequencies.__getitem__)
    if type(percentage) in (float, int):
        number = math.ceil(len(frequencies)*percentage/100)
    elif type(number) is int:
        pass
    else:
        raise ValueError("Either number or percentage must be provided!")

    words = words[:number]
    top = {word:frequencies[word] for word in words}
    return top


def word_frequencies(contents):
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
