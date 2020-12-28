from tkinter import *
import tkinter as tk
from tkinter.simpledialog import askstring
from googletrans import Translator
import random


translator = Translator()
mainwindow = Tk()
mainwindow.title('Obfuscator')
mainwindow.iconbitmap('assets/icon.ico')
mainwindow.geometry("649x450+553+314")
mainwindow.minsize(120, 1)
mainwindow.maxsize(3844, 1061)
mainwindow.resizable(1, 1)

text = Text(mainwindow)
text.place(relx=0.015, rely=0.022, relheight=0.698, relwidth=0.972)

with open('assets/languages.txt', 'rb') as languagefile:
    languages = languagefile.read()
    languages = languages.decode().split(",")


def obfuscate():
    global iterations
    global customlanguages

    inputtext = text.get('1.0', END)
    for i in range(0, iterations + 1):
        if i == iterations:
            destlanguage = 'en'

        elif customlanguages != 0:
            if customlanguages[i] == 'rand':
                destlanguage = random.choice(languages)
            else:
                destlanguage = customlanguages[i]
        else:
            destlanguage = random.choice(languages)

        translate = translator.translate(inputtext, dest=destlanguage)
        print('Translating to: ' + destlanguage + '.\n' + 'Output: ' + translate.text + '\n')
        inputtext = translate.text
        if i == iterations:
            outputwindow(translate.text)


def iterations():
    global iterations
    global customlanguages
    iterations = tk.simpledialog.askinteger(title='Iterations', prompt='Amount of iterations:')
    print('Amount of iterations set to', iterations)
    customlanguages = 0


def customlanguagesoption():
    global iterations
    global customlanguages
    customlanguages = tk.simpledialog.askstring(title='Custom languages', prompt='Custom languages:')
    customlanguages = customlanguages.split(' ')
    iterations = len(customlanguages)
    print('Automatically set iterations to', iterations)


def outputwindow(output):
    outputwindow = Toplevel()
    outputwindow.title("Output")
    outputwindow.iconbitmap('assets/icon.ico')
    TranslText = Text(outputwindow)
    TranslText.grid()
    TranslText.insert(END, output)
    buttonCpy = Button(outputwindow, height=3, width=80, text="Copy output", command=copyoutput(output))
    buttonCpy.grid()


def copyoutput(output):
    mainwindow.clipboard_clear()
    mainwindow.clipboard_append(output)


def moreoptions():
    print("Not finished yet")


Obfuscatebutton = Button(mainwindow, height=1, width=100, text='Obfuscate', command=obfuscate)
Customlangbutton = Button(mainwindow, height=1, width=100, text='Custom Languages', command=customlanguagesoption)
Iterationsbutton = Button(mainwindow, height=1, width=100, text='Iterations', command=iterations)
MoreOptionsbutton = Button(mainwindow, height=1, width=100, text='More options', command=moreoptions)

Obfuscatebutton.place(relx=0.015, rely=0.733, height=64, width=627)
Customlangbutton.place(relx=0.015, rely=0.889, height=44, width=207)
Iterationsbutton.place(relx=0.339, rely=0.889, height=44, width=207)
MoreOptionsbutton.place(relx=0.663, rely=0.889, height=44, width=207)

mainwindow.mainloop()
