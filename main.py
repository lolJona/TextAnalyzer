import csv
import tkinter as tk
from tkinter import filedialog
from collections import Counter
import string

# DEFAULTS
worddoc = ""
textbox = "Or add in your text here!"

# Some functions
def fileopener():
    global inputfile
    global worddoc
    inputfile = filedialog.askopenfilename()
    data = open(inputfile, 'r')
    worddoc = data.readlines()
    # f = open(inputfile)
    return data
    return worddoc
    return inputfile


def analyzer():
    global worddoc
    global count3
    global s2l
    nolists = str(worddoc)
    new_string = nolists.translate(str.maketrans('', '', string.punctuation))
    s2l = new_string.split()
    count2 = Counter(s2l)
    count3 = str(count2)
    return count3

def printoutput():
    global count3
    with open('output.txt', 'wt') as output:
        output.write(count3)

"""
START OF THE GUI
"""

class App(tk.Tk):
    def __init__(self):
        super().__init__()


        def textboxanalyzer():
            global textbox
            inputtext = str(self.addtext.get("1.0",'end-1c'))
            textstr = str(inputtext)
            newtextstr = textstr.translate(str.maketrans('', '', string.punctuation))
            nts2l = newtextstr.split()
            textcount = Counter(nts2l)
            textcount2 = str(textcount)
            with open('output.txt', 'wt') as output:
                output.write(textcount2)

        #Root Window
        self.title('Text Analyzer')
        self.geometry('600x420')

        #Main Frame
        self.frame = tk.Frame(self)
        self.headlabel = tk.Label(self, text="Text Analyzer", font="Katari 48")
        self.fileOpener = tk.Button(self, text="File to analyze", command=lambda: [fileopener()])
        self.txtLabel = tk.Label(self, text="NOTE: This app currently supports .txt files!", fg="red")
        self.testlabel = tk.Label(self, text="Optional features:")
        self.frequency = tk.Checkbutton(self, text="List frequency",)
        self.optional_no = tk.Checkbutton(self, text="No",)
        # OPTIONAL widgets
        self.newdelimlabel = tk.Label(self, text="New Delimiter:")
        self.newdelim = tk.Entry(self, width=2)
        self.outfile_error = tk.Label(self, text="This file already exists!", font="Calibri 9", fg="red")
        self.outfilename_label = tk.Label(self, text="New outfile name:")
        self.outfilename_entry = tk.Entry(self, width=30)
        self.addtext = tk.Text(self, height=12, width=50)
        self.textdata = tk.Button(self, text="Analyze textbox", command=textboxanalyzer)

        # NOT OPTIONAL
        self.convertButton = tk.Button(self, text="Examine File", command=lambda: [analyzer(), printoutput()])
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)

        self.frame.pack()
        self.headlabel.pack()
        self.fileOpener.pack()
        self.txtLabel.pack()
        self.testlabel.pack()
        self.frequency.pack()
        #self.optional_no.pack()
        #self.newdelimlabel.pack()
        #self.newdelim.pack()
        #self.outfile_error.pack()
        #self.outfilename_label.pack()
        #self.outfilename_entry.pack()
        self.convertButton.pack()
        self.addtext.pack(expand=True)
        self.addtext.insert('end', textbox)
        self.textdata.pack()
        self.quitButton.pack()

app = App()
app.mainloop()
