from tkinter import *
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.filedialog import askopenfilename
from googletrans import Translator
import random, json, pyperclip

mainwindow = Tk()
mainwindow.title('Obfuscator')
mainwindow.iconbitmap('assets/icon.ico')
mainwindow.geometry("649x450+553+314")
mainwindow.minsize(120, 1)
mainwindow.maxsize(3844, 1061)
mainwindow.resizable(1, 1)

proxyenabled = tk.IntVar()
proxystring = ""
customlanguages = ""
translatefilename= ""
langfilename = 'assets/languages.txt'
langamount = 85
iterationsdefined = ""

text = Text(mainwindow)
text.place(relx=0.015, rely=0.022, relheight=0.698, relwidth=0.972)
proxytext = Entry(mainwindow)
proxytext.place(relx=0.832, rely=0.756,height=20, relwidth=0.16)
proxytext.insert(END,'Proxy-Domain')

def obfuscate():
    global text
    global translatefilename
    
    if iterationsdefined == "":
        return tk.messagebox.showerror(title='Error', message="Please enter an amount of iterations first or specify languages")
    
    if len(text.get('1.0', 'end')) - 1 < 1:
       return tk.messagebox.showerror(title='Error', message="Please enter text before clicking the obfuscate button.")
    
    if proxyenabled.get() == 1:
        proxystring = proxytext.get()
        ProxyDict = {
                'https': proxystring
                }
        translator = Translator(proxies=ProxyDict)
    else:
        translator = Translator()
       
    openedfile = open(langfilename, 'r')
    openedfileread = openedfile.read()
    customlanguagesread = openedfileread.split(', ')
    if translatefilename != "":
        translatefileopen = open(translatefilename, 'r')
        originalText = translatefileopen.read()
    else:  
        
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
        translatedText = translator.translate(originalText, dest=languagesd)

        print('Output: ' + translatedText.text + '\n')
        originalText = translatedText.text
        global translatedText2
        translatedText2 = translator.translate(translatedText.text, dest='en')
        
    customnum = 0
    if translatefilename != "":
        translatefilename = ""
        text.delete('1.0',END)
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
    global iterationsdefined
    numberofiterations = int(iterationsprompt)
    if numberofiterations < 1:
        tk.messagebox.showerror(title='Error', message='Enter a number larger than 0')
        return iterations()
        
    customlanguages = ''
    iterationsdefined = "yes"
    print('Cleared custom languages in case any were set')
    print('Number of iterations set to ' + str(numberofiterations))

def customlanguagesoption():
    customlangprompt = askstring('Custom Languages', 'What custom languages do you want to use?')
    global customlanguages
    global numberofiterations
    global iterationsdefined
    if len(str(customlangprompt)) < 2:
        return tk.messagebox.showerror(title='Error', message="Input is too short to contain valid languages.")
    customlanguages = str(customlangprompt)
    numberofiterations = len(customlanguages.split(' '))
    iterationsdefined = "yes"
    print('Number of iterations automatically set to ' + str(numberofiterations))
    
def usecustomlanguagefile():
    global langfilename
    global langamount
    langfilenameask = askopenfilename(filetypes=(("Text File", "*.txt"),
                                              ("All files", "*.*") ))
    openedfile = open(langfilenameask,'r')
    openedfileread = openedfile.read()
    if len(openedfileread) < 2:
        return tk.messagebox.showerror(title='Error', message="Text in file is too short to contain correct languages.")

    customlanguagesread = openedfileread.split(', ')
    langfilename = langfilenameask
    print('Detected ' + str(len(customlanguagesread)) + ' entries in file. Successfully set custom language file.')

def filetranslate():
    global translatefilename
    translatefilenameask = askopenfilename(filetypes=(("Text File", "*.txt"),
                                              ("All files", "*.*") ))
    
    amountchars = len(open(translatefilenameask).read())
    if amountchars < 1:
        return tk.messagebox.showerror(title='Error',message='Document is empty. Cannot translate.')

    translatefilename = translatefilenameask

    print(translatefilename + ' selected')
    text.delete(1.0,END)
    text.insert(1.0,'Translating document')

def copyoutput():
    pyperclip.copy(translatedText2.text)

button1 = Button(mainwindow, height=1, width=100, text="Obfuscate", command=obfuscate)
button2 = Button(mainwindow, height=1, width=100, text="Custom Languages", command=customlanguagesoption)
buttonIT = Button(mainwindow, height=1, width=100, text="Iterations (All random)", command=iterations)
buttonClearCS = Button(mainwindow, height=1, width=100, text="Set Custom language file", command=usecustomlanguagefile)
buttonFileTR = Button(mainwindow, height=1, width=100, text="Translate File", command=filetranslate)
Proxybutton = tk.Checkbutton(mainwindow)

button1.place(relx=0.015, rely=0.733, height=64, width=527)
button2.place(relx=0.015, rely=0.889, height=44, width=157)
buttonIT.place(relx=0.262, rely=0.889, height=44, width=157)
buttonClearCS.place(relx=0.508, rely=0.889, height=44, width=157)
buttonFileTR.place(relx=0.755, rely=0.889, height=44, width=157)
Proxybutton.configure(text="Use proxy")
Proxybutton.configure(variable=proxyenabled, onvalue=1, offvalue=0)
Proxybutton.place(relx=0.832, rely=0.8, relheight=0.078, relwidth=0.16)


mainwindow.mainloop()


