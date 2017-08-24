# Hashtag Generator
This program searches the given text files and:
- Finds the most common words
- Lists the files in which they've been found
- Lists the sentences in which they've been found

## Setup
Note: this requires python 3.x to run.
Install requirements:
```bash
pip -r requirements.txt
```

Install nltk components (in a python shell):
```python
import nltk
nltk.download()
```
Install the brown corpus and the punkt tokeniser modules.

## Usage
Run:
```bash
./hashtagGen.py
```
No parameters are required, though if this were reused to use different sources, some optional parameters would be added.

## Output
I am using Tkinter to output the data. It should be fairly self-explanatory, although it is somewhat ugly.
