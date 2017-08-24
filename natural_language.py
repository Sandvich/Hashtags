from collections import Counter
from itertools import chain
from nltk.corpus import brown
from nltk import sent_tokenize
from nltk.tokenize import ToktokTokenizer
import math, string


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
    # Tuple of identifiers for connectives and other common words
    unwanted = ('at', 'to', 'in', 'ma', 'bez', 'ppss', 'pp$', 'dt', 'bedz', 'hv', 'cc', 'cs', 'hvd', 'wdt', '*', 'bed',
                'ber', 'be', 'np$', 'ppo', 'pps', 'abn', 'cd', 'md', 'ben', 'ben', 'wps', 'vbd', 'jj', 'rb', 'do', 'ql',
                'dts', 'rp', 'in-tl', 'ex', 'i', 'dti', 'dod', 'wrb', 'hvz', 'nn$')
    # This is far from the best way to do this, but I couldn't find the documentation for these identifiers
    frequencies = {}
    for key in keys:
        total = 0
        if (key[0] not in string.punctuation) and (key.split('/')[-1] not in unwanted):  # Gets rid of unwanted tokens
            for sublist in list:
                if key in sublist.keys():
                    total += sublist[key]
            frequencies[key.split('/')[0].lower()] = total
    print("Total words (that we care about): " + str(len(frequencies.keys())))

    return frequencies
