from googletrans import Translator, constants
from subprocess import check_output
from tkinter import *

def translator():
    text=check_output(["xclip", "-o"]).decode()
    trans = Translator()
    translation = trans.translate(text, dest="it")
    translation.text
    count=0
    formatted=""
    for ch in list(translation.text):
        count += 1
        if count == 55:
            count=0
            formatted += "\n"
        formatted += ch
    return formatted

def gui():
    window = Tk()
    window.geometry("400x400+55+400")
    window.overrideredirect(True)
    text=translator()
    text_label = Label(window, text=text).place(x=0, y=0)
    window.bind("<Button-1>", exit)
    
    window.mainloop()

if __name__ == "__main__":
    gui()
