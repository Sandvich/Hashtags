import re
from nltk import tokenize


def files_word(file_contents, to_search):
    """Searches the file contents for specific words and returns a list of which files each word appears in."""
    files = []

    for word in to_search:
        files.append([])
        pattern = re.compile("[^a-z]" + word + "[^a-z]")
        # The pattern that I use here is intended to avoid partial word matches
        for filename in sorted(file_contents.keys()):
            if pattern.search(file_contents[filename].lower()) is not None:
                files[-1].append(filename)
        item = list_to_string(files.pop())
        files.append(item)

    return files


def sentences_word(string_contents, to_search):
    """Searches the file contents for specific words and returns a list of sentences each word appears in."""
    sentences = []

    # Convert each document to sentences
    for document in string_contents.keys():
        string_contents[document] = tokenize.sent_tokenize(string_contents[document])

    for word in to_search:
        sentences.append([])
        pattern = re.compile("[^a-z]" + word + "[^a-z]")
        for document in sorted(string_contents.keys()):
            for sentence in string_contents[document]:
                if pattern.search(sentence) is not None:
                    sentences[-1].append(sentence)
        item = list_to_string(sentences.pop())
        sentences.append(item)

    return sentences


def list_to_string(list: list):
    string = ""
    for item in list:
        string += str(item) + "\n"
    string = string[:-1]
    return string
