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
No parameters are required, though if this were reused to use different sources, some optional parameters would be
added.

## Output
I am using Tkinter to output the data. It should be fairly self-explanatory, although it is somewhat ugly.<br>
Tkinter is a quick and dirty graphical output. If I took more time about this, I would potentially use Flask's
templating tools, QT or ncurses to make something not quite so ugly.<br><br>
For some reason, the term "af" sometimes appears in the output. Given more time I would investigate this, but it seems
to be a bug in the tokeniser. Additionally, given more time I would make a cleaner process for getting rid of dead
words, as the method I used was very crude (see natural_language.py lines 50 onwards). I also think it would be 
worthwhile to find a better method for searching through the text than regex, as the regex isn't quite so reliable (see
the results for the word "I" for an example).<br><br>
I didn't bother to sort the dictionary used for the frequency distribution when printing to console, though because this
is debug information I don't think it is an issue.
