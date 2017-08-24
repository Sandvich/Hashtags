from string_input import txt_file_import
from natural_language import word_frequencies, top_frequencies
from data_process import files_word, sentences_word
from tabulate import tabulate


def main():
    contents = txt_file_import()
    #print(contents.keys())

    # Count the frequency of each word that appears in the files, and select the top 5
    top_unsorted = top_frequencies(word_frequencies(contents), number=10)
    top = sorted(top_unsorted, reverse=True, key=top_unsorted.__getitem__)
    print("Final frequency graph:\n" + str(top))

    # For each word in this list, find which documents it appears in and which sentences it appears in.
    table = [top, files_word(contents, top), sentences_word(contents, top)]
    print(tabulate(table, ("Word", "Documents", "Sentences"), "pipe"))


if __name__ == "__main__":
    main()
