from string_input import txt_file_import
from natural_language import word_frequencies, top_frequencies
from data_process import files_word, sentences_word
from display import run


def main():
    contents = txt_file_import()
    to_print = ["Files imported:"] + list(contents.keys())
    print(*to_print)

    # Count the frequency of each word that appears in the files, and select the top 5
    top = top_frequencies(word_frequencies(contents), number=5)
    print("Final frequency graph:\n" + str(top))

    # For each word in this list, find which documents it appears in and which sentences it appears in.
    table = [sorted(top.keys(), reverse=True, key=top.__getitem__),
             files_word(contents, top),
             sentences_word(contents, top)]

    print("Building UI")
    run(table)


if __name__ == "__main__":
    main()
