import os, string


def txt_file_import():
    '''Imports all txt files in the current directory (ignoring requirements.txt if it exists)'''
    # Generate a list of files in the current directory with the extension "txt"
    txt_files = [ name for name in os.listdir(os.curdir) if (os.path.isfile(name) and name.split('.')[-1] == "txt") ]
    if "requirements.txt" in txt_files:
        txt_files.remove("requirements.txt")

    # Copy the contents into a dictionary (keys being the file name), removing punctuation (other than -) and setting
    # all the text to lowercase
    contents = {}
    translate_table = {ord(char): None for char in string.punctuation}
    translate_table['-']='-'
    for name in txt_files:
        f = open(name,'r')
        contents[name] = f.read().translate(translate_table).lower()
        f.close()
    return contents
