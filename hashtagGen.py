import nltk
import os


def copy_contents(files):
    contents = {}
    for name in files:
        f = open(name,'r')
        contents[name] = f.readlines()
        f.close()
    return contents


def main():
    txt_files = [ name for name in os.listdir(os.curdir) if (os.path.isfile(name) and name.split('.')[-1] == "txt") ]
    if "requirements.txt" in txt_files:
        txt_files.remove("requirements.txt")

    contents = copy_contents(txt_files)
    print(contents.keys())


if __name__ == "__main__":
    main()
