from string_input import txt_file_import
from natural_language import word_frequencies, top_frequencies


def main():
    contents = txt_file_import()
    #print(contents.keys())

    # Count the frequency of each word that appears in the files, and select the top 5
    top_unsorted = top_frequencies(word_frequencies(contents), number=10)
    top = sorted(top_unsorted, reverse=True, key=top_unsorted.__getitem__)
    print("Final frequency graph:\n" + str(top))

    # For each word in this list, do some stuff


if __name__ == "__main__":
    main()
