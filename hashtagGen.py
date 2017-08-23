import nltk
import os
from string_input import txt_file_import


def main():
    contents = txt_file_import()
    print(contents.keys())

    # Count the frequency of each word that appears in the files
    words = {}

    # Select only the top 5%
    # For each word in this list, do some stuff


if __name__ == "__main__":
    main()
