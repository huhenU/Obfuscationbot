from tkinter import *
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

customlanguages = ""
translatefilename= ""
langfilename = 'assets/languages.json'
langamount = 85

text = Text(mainwindow)
text.place(relx=0.017, rely=0.022, relheight=0.698, relwidth=0.957)

def obfuscate():
    print(customlanguages)
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
    langfilename = askopenfilename(filetypes=(("JSON File", "*.json"),
                                              ("All files", "*.*") ))
    with open(langfilename) as lang_strings:
        data = json.load(lang_strings)
        langamount = len(data)
        print('Detected ' + str(langamount) + ' entries in file. Successfully set custom language file.')

def filetranslate():
    global translatefilename
    translatefilename = askopenfilename(filetypes=(("Text File", "*.txt"),
                                              ("All files", "*.*") ))
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
button1.place(relx=0.017, rely=0.733, height=64, width=577)
button2.place(relx=0.017, rely=0.889, height=44, width=157)
buttonIT.place(relx=0.283, rely=0.889, height=44, width=147)
buttonClearCS.place(relx=0.533, rely=0.889, height=44, width=147)
buttonFileTR.place(relx=0.783, rely=0.889, height=44, width=117)

mainwindow.mainloop()


