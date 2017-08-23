from string_input import txt_file_import
from natural_language import word_frequencies, top_frequencies


def main():
    contents = txt_file_import()
    print(contents.keys())

    # Count the frequency of each word that appears in the files
    frequencies = word_frequencies(contents)

    # Select only the top 1%
    frequencies = top_frequencies(frequencies, percentage=1)
    print("Final frequency graph:\n" + str(frequencies))

    # For each word in this list, do some stuff


if __name__ == "__main__":
    main()
