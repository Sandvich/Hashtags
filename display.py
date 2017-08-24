from tkinter import *
from tkinter import ttk

def run(data):
    root = Tk()
    root.title("Hashtag Gen")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Word").grid(row=0, column=0, sticky=W)
    ttk.Label(mainframe, text="Documents").grid(row=0, column=1, sticky=W)
    ttk.Label(mainframe, text="Sentences").grid(row=0, column=2, sticky=W, columnspan=2)

    for i, word in enumerate(data[0]):
        ttk.Label(mainframe, text=word).grid(row=i+1, column=0, sticky=(N,W))
        ttk.Label(mainframe, text=data[1][i]).grid(row=i+1, column=1, sticky=(N,W))
        sentences = Text(mainframe, width=100, height=10)
        sentences.insert("1.0", data[2][i])
        scroll = ttk.Scrollbar(mainframe, orient=VERTICAL, command=sentences.yview)
        sentences.configure(yscrollcommand=scroll.set, wrap="word", state="disabled")
        sentences.grid(row=i+1, column=2, sticky=(W,E))
        scroll.grid(row=i+1, column=3, sticky=(N,S,W))

    root.mainloop()
