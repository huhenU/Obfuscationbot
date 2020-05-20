from tkinter import *
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.filedialog import askopenfilename
from googletrans import Translator
import random, json, pyperclip
translator = Translator()
mainwindow = Tk()
mainwindow.title('Obfuscator')
mainwindow.iconbitmap('assets/icon.ico')
mainwindow.geometry("600x450+536+292")
mainwindow.minsize(120, 1)
mainwindow.maxsize(3844, 1061)
mainwindow.resizable(1, 1)

proxyenabled = tk.IntVar()
proxystring = ""
customlanguages = ""
translatefilename= ""
langfilename = 'assets/languages.txt'
langamount = 85

text = Text(mainwindow)
text.place(relx=0.017, rely=0.022, relheight=0.698, relwidth=0.957)

def obfuscate():    
    openedfile = open(langfilename, 'r')
    openedfileread = openedfile.read()
    customlanguagesread = openedfileread.split(', ')
    print(customlanguagesread)
    if translatefilename != "":
        translatefileopen = open(translatefilename, 'r')
        originalText = translatefileopen.read()
    else:  
        global text
        originalText = text.get("1.0", "end")
    global customnum
    customnum = 0
    for i in range(numberofiterations):
        if customlanguages != "":
            forcelanguage = customlanguages.split(' ')
            languagesd = forcelanguage[customnum]
            if languagesd == "rand":
                languagesd = random.choice(customlanguagesread)
            customnum += 1
        else:
            languagesd = random.choice(customlanguagesread)
            
        print('Translating to language: ' + languagesd)
        if proxyenabled.get() == 1:
            ProxyDict = {
                'https': proxystring
                }
            translatorProxy = Translator(proxies=ProxyDict)
            translatedText = translatorProxy.translate(originalText, dest=languagesd)
        else:
            translator = Translator()
            translatedText = translator.translate(originalText, dest=languagesd)
        print('Output: ' + translatedText.text + '\n')
        originalText = translatedText.text
        global translatedText2
        if proxyenabled.get() == 1:
            translatorProxy = Translator(proxies=ProxyDict)
            translatedText2 = translatorProxy.translate(translatedText.text, dest='en')
        else:
            translator = Translator()
            translatedText2 = translator.translate(translatedText.text, dest='en')
        
    customnum = 0
    print('Final output: ' + translatedText2.text)
    outputwindow = Toplevel()
    outputwindow.title("Obfuscated text")
    outputwindow.iconbitmap('assets/icon.ico')
    TranslText = Text(outputwindow)
    TranslText.grid()
    TranslText.insert(END, translatedText2.text)
    buttonCpy = Button(outputwindow, height=3, width=80, text="Copy Output", command=copyoutput)
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
    
def usecustomlanguagefile():
    global langfilename
    global langamount
    langfilename = askopenfilename(filetypes=(("Text File", "*.txt"),
                                              ("All files", "*.*") ))
    openedfile = open(langfilename,'r')
    openedfileread = openedfile.read()
    customlanguagesread = openedfileread.split(', ')
    print('Detected ' + str(len(customlanguagesread)) + ' entries in file. Successfully set custom language file.')

def filetranslate():
    global translatefilename
    translatefilename = askopenfilename(filetypes=(("Text File", "*.txt"),
                                              ("All files", "*.*") ))
    print(translatefilename + ' selected')
    text.delete(1.0,END)
    text.insert(1.0,'Translating document')

def copyoutput():
    pyperclip.copy(translatedText2.text)

def setproxy():
    if proxyenabled.get() == 1:
        proxyprompt = askstring('Proxy', "Enter your Proxy domain")
        global proxystring
        proxystring = proxyprompt
        return print('Proxy successfully set to ' + proxystring)

button1 = Button(mainwindow, height=1, width=100, text="Obfuscate", command=obfuscate)
button2 = Button(mainwindow, height=1, width=100, text="Custom Languages", command=customlanguagesoption)
buttonIT = Button(mainwindow, height=1, width=100, text="Iterations (All random)", command=iterations)
buttonClearCS = Button(mainwindow, height=1, width=100, text="Set Custom language file", command=usecustomlanguagefile)
buttonFileTR = Button(mainwindow, height=1, width=100, text="Translate File", command=filetranslate)
Checkbutton1 = tk.Checkbutton(mainwindow)
button1.place(relx=0.017, rely=0.733, height=64, width=497)
button2.place(relx=0.017, rely=0.889, height=44, width=147)
buttonIT.place(relx=0.267, rely=0.889, height=44, width=147)
buttonClearCS.place(relx=0.517, rely=0.889, height=44, width=147)
buttonFileTR.place(relx=0.767, rely=0.889, height=44, width=127)
Checkbutton1.configure(text="Use proxy")
Checkbutton1.configure(variable=proxyenabled, onvalue=1, offvalue=0, command=setproxy)
Checkbutton1.place(relx=0.85, rely=0.778, relheight=0.056, relwidth=0.133)


mainwindow.mainloop()


