from tkinter import *
from tkinter.simpledialog import askstring
from googletrans import Translator
from tkinter.filedialog import askopenfilename
import random
import json
import pyperclip
translator = Translator()
mainwindow = Tk()
mainwindow.title('Obfuscator')
mainwindow.iconbitmap('assets/icon.ico')

customlanguages = ""
langfilename = 'assets/languages.json'
langamount = 85

text=Text(mainwindow)
text.grid()

def obfuscate():
    print(customlanguages)
    global text
    originalText = text.get("1.0", "end")
    global customnum
    customnum = 0
    for i in range(numberofiterations):
        if customlanguages != "":
            forcelanguage = customlanguages.split(' ')
            languagesd = forcelanguage[customnum]
            if languagesd == "rand":
                language = random.randint(1, langamount)
                with open(langfilename) as lang_strings:
                    data = json.load(lang_strings)
                    languagesd = data[str(language)]
            customnum += 1
        else:
            language = random.randint(1, langamount)
        with open(langfilename) as lang_strings:
            data = json.load(lang_strings)
            if customlanguages == "":
                languagesd = data[str(language)]
            print('Translating to language: ' + languagesd)
            translatedText = translator.translate(originalText, dest=languagesd)
            print('Output: ' + translatedText.text + '\n')
            originalText = translatedText.text
            global translatedText2
            translatedText2 = translator.translate(translatedText.text, dest='en')
            
    customnum = 0
    print('Final output: ' + translatedText2.text)
    outputwindow = Toplevel()
    outputwindow.title("Obfuscated text")
    outputwindow.iconbitmap('assets/icon.ico')
    TranslText = Text(outputwindow)
    TranslText.grid()
    TranslText.insert(END, translatedText2.text)
    buttonCpy = Button(outputwindow, height=1, width=50, text="Copy Output", command=copyoutput)
    buttonCpy.grid()

def iterations():
    iterationsprompt = askstring('Iterations', "Enter the amount of iterations")
    global numberofiterations
    global customlanguages
    numberofiterations = int(iterationsprompt)
    customlanguages = ''
    print('Cleared custom languages in case any were set')
    print('Number of iterations set to ' + str(numberofiterations))

def customlanguagesoption():
    customlangprompt = askstring('Custom Languages', 'What custom languages do you want to use?')
    global customlanguages
    global numberofiterations
    customlanguages = str(customlangprompt)
    numberofiterations = len(customlanguages.split(' '))
    print('Number of iterations automatically set to ' + str(numberofiterations))
    

def moreoptions():
    optionwindow = Toplevel()
    optionwindow.title('Options')
    optionwindow.iconbitmap('assets/icon.ico')
    buttonIT = Button(optionwindow, height=2, width=25, text="Iterations (All random)", command=iterations)
    buttonCS = Button(optionwindow, height=2, width=25, text="Custom Languages", command=customlanguagesoption)
    buttonClearCS = Button(optionwindow, height=2, width=25, text="Set Custom language file", command=usecustomlanguagefile)
    buttonIT.grid()
    buttonCS.grid()
    buttonClearCS.grid()

def usecustomlanguagefile():
    global langfilename
    global langamount
    langfilename = askopenfilename(filetypes=(("JSON File", "*.json"),
                                              ("All files", "*.*") ))
    with open(langfilename) as lang_strings:
        data = json.load(lang_strings)
        langamount = len(data)
        print('Detected ' + str(langamount) + ' entries in file. Successfully set custom language file.')

def copyoutput():
    pyperclip.copy(translatedText2.text)

button1 = Button(mainwindow, height=1, width=100, text="Obfuscate", command=obfuscate)
button2 = Button(mainwindow, height=1, width=100, text="Options and Iterations", command=moreoptions)
button1.grid()
button2.grid()

mainwindow.mainloop()


